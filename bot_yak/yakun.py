import asyncio
import sqlite3
from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, \
    CallbackQuery, BotCommand
from aiogram.types import BufferedInputFile
import matplotlib.pyplot as plt
from io import BytesIO

bot = Bot(token='7685705773:AAHRHRcxaIUTtXVNCqVCqA8X7QkaRF9xbdw')
dp = Dispatcher()
chat_id = "@bobomurodbeckend"
chat_idbot = "@pythonbeckend_bot"
user_data={}

admin_id=[5652442685]

@dp.message(Command("topchart"))
async def top_chart(message: Message):
    if message.from_user.id not in admin_id:
        await message.answer("❌ Bu buyruq faqat adminlar uchun.")
        return
    cursor.execute("""
        SELECT invited_by, COUNT(*) as count 
        FROM users 
        WHERE invited_by IS NOT NULL 
        GROUP BY invited_by 
        ORDER BY count DESC 
        LIMIT 5
    """)
    top = cursor.fetchall()

    if not top:
        await message.answer("Hozircha statistik ma'lumot yo'q.")
        return

    users = [str(user[0]) for user in top]
    counts = [user[1] for user in top]

    plt.figure(figsize=(10, 6))
    plt.bar(users, counts, color='skyblue')
    plt.xlabel("Foydalanuvchi ID")
    plt.ylabel("Taklif qilganlar soni")
    plt.title("Top 5 referal foydalanuvchilar")
    plt.tight_layout()

    buf = BytesIO()

    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()

    photo = BufferedInputFile(buf.read(), filename="chart.png")
    await message.answer_photo(photo, caption="🏆 TOP 5 foydalanuvchilar grafigi")



conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Foydalanuvchi ma'lumotlari jadvali
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    phone_number TEXT,
    points INTEGER DEFAULT 0,
    invited_by INTEGER
)
""")
conn.commit()

async def commanda():
    command=[
        BotCommand(command='/start', description="Botni ishga tushurish"),
        BotCommand(command="/topchart", description="Statistika")
    ]
    await bot.set_my_commands(command)

@dp.message(Command("start"))
async def catch_command(message: Message):
    user_id = message.from_user.id
    args = message.text.split()

    invited_by = None
    if len(args) > 1 and args[1].isdigit():
        invited_by = int(args[1])

    # Agar foydalanuvchi oldin bazada bo'lmasa, qo‘shamiz
    cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    user = cursor.fetchone()

    if not user:
        cursor.execute("INSERT INTO users (user_id, phone_number, invited_by, points) VALUES (?, ?, ?, ?)",
                       (user_id, None, invited_by, 0))
        conn.commit()


    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📲Telefon raqamni yuborish",request_contact=True)],
        ],
        resize_keyboard=True,one_time_keyboard=True
    )
    await message.answer("📌 Iltimos, telefon raqamingizni yuboring:", reply_markup=keyboard)


@dp.message(lambda message: message.contact)
async def get_contact(message: Message):
    user_id = message.from_user.id
    contact_number = message.contact.phone_number

    cursor.execute("SELECT invited_by FROM users WHERE user_id=?", (user_id,))
    user = cursor.fetchone()

    if user:
        invited_by = user[0]
    else:
        invited_by = None

    # Foydalanuvchi raqamini yangilash
    cursor.execute("UPDATE users SET phone_number = ? WHERE user_id = ?", (contact_number, user_id))
    conn.commit()

    # 🔥 Yangi kod: Agar foydalanuvchi birinchi marta kirayotgan bo‘lsa, points qo‘shamiz
    if invited_by is not None:
        cursor.execute("SELECT COUNT(*) FROM users WHERE invited_by=? AND user_id=?", (invited_by, user_id))
        already_counted = cursor.fetchone()[0]

        if already_counted == 0:  # 🔹 Agar bu ID bo‘yicha points qo‘shilmagan bo‘lsa
            cursor.execute("UPDATE users SET points = points + 1 WHERE user_id=?", (invited_by,))
            conn.commit()

    keybord = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📝Kanalga qo'shilish",url=f"https://t.me/{chat_id.strip('@')}")],
            [InlineKeyboardButton(text="✅Obunani tekshirish",callback_data="tekshirish")]
        ]
    )
    await message.answer("📌 Avval kanalga obuna bo‘ling va \n"
                         "Obunani tekshirish' tugmasini bosing:",reply_markup=keybord)


@dp.callback_query(lambda callback: callback.data == "tekshirish")
async def check_subscription(callback: CallbackQuery):
    user_id = callback.from_user.id
    user_link = f"https://t.me/{chat_idbot.strip('@')}?start={user_id}"
    chat_member = await bot.get_chat_member(chat_id, user_id)
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="💻Nega siz python tanlashiz kerak"),KeyboardButton(text="🗒Python kurslar ro'yxati")],
            [KeyboardButton(text="📊 Mening hisobim"), KeyboardButton(text="🔗Referal Link")]
        ],
        resize_keyboard=True
    )
    await callback.message.answer(text=chat_member.status, reply_markup=keyboard)

    if chat_member.status in ["member", "administrator", "creator"]:
        await callback.message.answer("🎉 Siz kanalga a'zo bo'dingiz!\n\n"
                                      "🔗Bu sizning referal linkingiz\n"
                                      f"🟦{user_link}\n"
                                      "👥 Siz bu yerda python beckenda aloqador narsalarni topishingiz mumkin!")
    else:
        await callback.message.answer("❌ Siz hali kanalga a'zo bo‘lmadingiz! Iltimos, kanalga obuna bo‘ling.")


@dp.message(lambda message: message.text == "📊 Mening hisobim")
async def send_link(message: Message):
    user_id = message.from_user.id
    phone_nuber = user_data.get(user_id,{}).get("phone_number","mavjud emas")
    cursor.execute("SELECT phone_number, points FROM users WHERE user_id=?", (user_id,))
    user = cursor.fetchone()
    if user:
        phone_number, points = user
    else:
        phone_number, points = "Mavjud emas", 0
    await message.answer  (f"🎯 Your Points:{points}\n"
                          f"💬 Your ID:{user_id}\n"
                          f"👥 Friends Invited:{points} people\n"
                          f"📱 Account Number:{phone_nuber}")

@dp.message(lambda message: message.text == "🔗Referal Link")
async def send_link(message: Message):
    user_id = message.from_user.id
    user_link = f"https://t.me/{chat_idbot.strip('@')}?start={user_id}"
    await message.answer(f"👤{message.from_user.full_name} ,bu yerda sizning referal linkingiz \n\n"
                         f"🔗{user_link}"
                         )

@dp.message(lambda message: message.text =="💻Nega siz python tanlashiz kerak")
async def switch_to_channel(message:Message):
    keybor=InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Python boshlang'ich bazi narsalar", url="https://t.me/bobomurodbeckend/11")],
            [InlineKeyboardButton(text='Nega aynan python',url="https://mohirdev.uz/blog/frontend-yoki-bekend-dasturlashning-qaysi-yolidan-borgan-maqul/")],
            [InlineKeyboardButton(text="Python beckendchi bo'lish uchun nimalarni bilish kerak",url="https://t.me/bobomurodbeckend/16")],
            [InlineKeyboardButton(text="Python beckendi bolish uchun o'rganish kerak bo'lgan narsalar",url="https://t.me/bobomurodbeckend/20, https://t.me/bobomurodbeckend/21")],
            [InlineKeyboardButton(text="Data science bo'lish uchun nimlaeni bilish kerak", url="https://t.me/bobomurodbeckend/12")],

        ]

    )
    await message.answer(text="🖲Siz uchun kerakli bo'lgan tugmani bosing", reply_markup=keybor)


@dp.message(lambda message:message.text == "🗒Python kurslar ro'yxati")
async def curs(message:Message):
    keybord = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="💻Online kurslar",callback_data="connect1")],
            [InlineKeyboardButton(text="🏫Offline kurslar", callback_data="connect2")]
        ]
    )
    await message.answer(text="🖲Sizga ma'qul kelgan tugamni bosing", reply_markup=keybord)

@dp.callback_query(lambda callback_query: callback_query.data == "connect1")
async def kurs(callback_query: CallbackQuery):
    url = [
        "https://praktikum.mohirdev.uz/dashboard",
        "https://vk.cc/atUpWc",
        "https://clck.ru/MLAja"
    ]

    text = (
        f"[Mohirdev]({url[0]})\n"
        f"[GeekBrains]({url[1]})\n"
        f"[beONmax]({url[2]})\n\n"
        "Siz o‘zingizga ma’qulini ko‘rib chiqishingiz mumkin."
    )

    await callback_query.message.answer(text, parse_mode=ParseMode.MARKDOWN)

@dp.callback_query(lambda callback_query: callback_query.data == "connect2")
async def kurs(callback_query: CallbackQuery):
    url = [
            "https://kurslar.najottalim.uz/python",
        "https://www.soffstudy.uz/courses",
        "https://proweb.uz/uz/courses/python",

    ]
    text = (
        f"[Najot ta'lim]({url[0]})\n"
        f"[Soff Study]({url[1]})\n"
        f"[ProWeb]({url[2]})"
        f"Siz o'ziga ma'qul kelgan o'quv markazlarini ko'rishingiz mumkin"
    )
    await callback_query.message.answer(text, parse_mode=ParseMode.MARKDOWN)
async def main():
    await commanda()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

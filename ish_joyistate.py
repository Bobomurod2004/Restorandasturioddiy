from aiogram import Router,Bot, types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message,InlineKeyboardMarkup,InlineKeyboardButton, CallbackQuery
from State_s import Ish_joyi

router = Router()

@router.message(lambda message:message.text == "Ish joyi kerak")
async def ish_joyi(message: Message, state:FSMContext):
    await message.answer("Ism, Familiyangizni kiriting")
    await state.set_state(Ish_joyi.name)

@router.message(Ish_joyi.name)
async def ish_joyi_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Bu yerga yoshungizni kiriting")
    await state.set_state(Ish_joyi.age)

@router.message(Ish_joyi.age)
async def ish_joyi_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("bu yerga siz texnologiyagni kiriting")
    await state.set_state(Ish_joyi.texnology)

@router.message(Ish_joyi.texnology)
async def ish_joyi_texno(message:Message,state:FSMContext):
    await state.update_data(texnology=message.text)
    await message.answer("Siz bu yerga aloqani kiriting")
    await state.set_state(Ish_joyi.aloqa)

@router.message(Ish_joyi.aloqa)
async def ish_joyi_aloqa(message:Message, state: FSMContext):
    await state.update_data(aloqa=message.text)
    await message.answer("siz bu yerga hududni kiriting")
    await state.set_state(Ish_joyi.hudud)

@router.message(Ish_joyi.hudud)
async def ish_joyi_hudud(message:Message, state: FSMContext):
    await state.update_data(hudud=message.text)
    await message.answer("siz bu yerga tolov summasi kiriting")
    await state.set_state(Ish_joyi.tolov)

@router.message(Ish_joyi.tolov)
async def ish_joyi_tolov(message:Message, state: FSMContext):
    await state.update_data(tolov=message.text)
    await message.answer("siz bu yerga kasbini kiriting")
    await state.set_state(Ish_joyi.kasbi)

@router.message(Ish_joyi.kasbi)
async def ish_joyi_aloqa(message:Message, state: FSMContext):
    await state.update_data(kasbi=message.text)
    await message.answer("siz bu yerga murojat vaqtini kiriting")
    await state.set_state(Ish_joyi.murojat)

@router.message(Ish_joyi.murojat)
async def ish_joyi_aloqa(message:Message, state: FSMContext):
    await state.update_data(murojat=message.text)
    await message.answer("siz bu yerga maqsadingizni  kiriting")
    await state.set_state(Ish_joyi.maqsad)

@router.message(Ish_joyi.maqsad)
async def ish_joyi_maqsad(message: Message,state: FSMContext):
    user_date = await state.get_data()
    keybord = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="ha", callback_data="ha"), InlineKeyboardButton(text="yo'q",callback_data="yo'q")]
        ]
    )


    result_text = ("ish joyi kerak\n\n"
                   f"Ism{user_date["name"]}\n"
                   f"Yoshi{user_date.get("age")}\n"
                   f"texnologiya{user_date.get("texnoliyg")}\n"
                   f"aloqa {user_date.get("aloqa")}\n"
                   f"hudud {user_date.get("hudud")}\n"
                   f"tolov {user_date.get("tolov")}\n"
                   f"kasbi {user_date.get("kasbi")}\n"
                   f"murojat {user_date.get("murojat")}\n"
                   f"maqsad {message.text}")
    await message.answer(result_text,reply_markup=keybord)
    await state.clear()

@router.callback_query(lambda callback: callback.data == "ha")
async def send_result(callback: CallbackQuery):
    result_text = "callback.message.text"

    await callback.bot.send_message(
        chat_id=5859017460,
        text= result_text
    )
    await callback.message.answer("✅ Ma’lumot yuborildi!")


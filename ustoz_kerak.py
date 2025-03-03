from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from State_s import Ustoz

router = Router()

@router.message(lambda message:message.text == "Ustoz kerak")
async def ish_joyi(message: Message, state:FSMContext):
    await message.answer("Ism, Familiyangizni kiriting")
    await state.set_state(Ustoz.name)

@router.message(Ustoz.name)
async def ish_joyi_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Bu yerga yoshungizni kiriting")
    await state.set_state(Ustoz.age)

@router.message(Ustoz.age)
async def ish_joyi_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("bu yerga siz texnologiyagni kiriting")
    await state.set_state(Ustoz.texnology)

@router.message(Ustoz.texnology)
async def ish_joyi_texno(message:Message,state:FSMContext):
    await state.update_data(texnology=message.text)
    await message.answer("Siz bu yerga aloqani kiriting")
    await state.set_state(Ustoz.aloqa)

@router.message(Ustoz.aloqa)
async def ish_joyi_aloqa(message:Message, state: FSMContext):
    await state.update_data(aloqa=message.text)
    await message.answer("siz bu yerga hududni kiriting")
    await state.set_state(Ustoz.hudud)

@router.message(Ustoz.hudud)
async def ish_joyi_hudud(message:Message, state: FSMContext):
    await state.update_data(hudud=message.text)
    await message.answer("siz bu yerga tolov summasi kiriting")
    await state.set_state(Ustoz.tolov)

@router.message(Ustoz.tolov)
async def ish_joyi_tolov(message:Message, state: FSMContext):
    await state.update_data(tolov=message.text)
    await message.answer("siz bu yerga kasbini kiriting")
    await state.set_state(Ustoz.kasbi)

@router.message(Ustoz.kasbi)
async def ish_joyi_aloqa(message:Message, state: FSMContext):
    await state.update_data(kasbi=message.text)
    await message.answer("siz bu yerga murojat vaqtini kiriting")
    await state.set_state(Ustoz.murojat)

@router.message(Ustoz.murojat)
async def ish_joyi_aloqa(message:Message, state: FSMContext):
    await state.update_data(murojat=message.text)
    await message.answer("siz bu yerga maqsadingizni  kiriting")
    await state.set_state(Ustoz.maqsad)

@router.message(Ustoz.maqsad)
async def ish_joyi_maqsad(message: Message,state: FSMContext):
    user_date = await state.get_data()


    result_text = ("Ustoz  kerak\n\n"
                   f"Ism{user_date["name"]}\n"
                   f"Yoshi{user_date.get("age")}\n"
                   f"texnologiya{user_date.get("texnoliyg")}\n"
                   f"aloqa {user_date.get("aloqa")}\n"
                   f"hudud {user_date.get("hudud")}\n"
                   f"tolov {user_date.get("tolov")}\n"
                   f"kasbi {user_date.get("kasbi")}\n"
                   f"murojat {user_date.get("murojat")}\n"
                   f"maqsad {message.text}")
    await message.answer(result_text)
    await state.clear()
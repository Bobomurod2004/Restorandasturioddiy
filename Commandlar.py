from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from tugamalar import menu_keyboard

router=Router()

@router.message(Command("start"))
async def start(messgae: Message):
    await messgae.answer("salam men telgram botman "
                         "sizga qanday yordam bera olaman")


@router.message(Command("menu"))
async def menu(message: Message):
    keybord = menu_keyboard()
    await message.answer(text="Siz o'zizga mas keladigan ",reply_markup=keybord)

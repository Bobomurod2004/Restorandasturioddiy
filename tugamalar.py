from aiogram import Router
from aiogram.types import Message,ReplyKeyboardMarkup,KeyboardButton

def menu_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Ish joyi kerak", callback_data="1button"),
             KeyboardButton(text="Xodim kerak", callback_data="2button")],
            [KeyboardButton(text="Sherik kerak", callback_data="3button"),
             KeyboardButton(text="Ustoz kerak", callback_data="4button")]

        ],
        resize_keyboard=True
    )


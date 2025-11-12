from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard_1 = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="📍 Lokatsiyani yuborish", request_location=True),
            KeyboardButton(text="📲 Telifon raqamni yuborish", request_contact=True)
        ],
        [KeyboardButton(text="/start")
         ]
    ]
)
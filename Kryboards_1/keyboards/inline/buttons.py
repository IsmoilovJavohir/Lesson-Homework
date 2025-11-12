from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


inline_keyboard = [[
    InlineKeyboardButton(text="✅ Yes", callback_data='yes'),
    InlineKeyboardButton(text="❌ No", callback_data='no')
]]
are_you_sure_markup = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)

inline_joxa = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📍 Lokatsiyani yuborish", callback_data='lokatsiyani_yuborish')],
    [InlineKeyboardButton(text="📲 Telifon raqamni yuborish",callback_data='telifon_raqamni_yuborish')],
    [InlineKeyboardButton(text="🎶YouTube musc", url="https://youtu.be/4c2dB6YtPqc?si=4S-n2_k2iN41UDh6"),
     InlineKeyboardButton(text="ChatGPT🔮", url="https://chatgpt.com/")]
])
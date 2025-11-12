from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.session.middlewares.request_logging import logger
from loader import bot
from data.config import ADMINS
from utils.extra_datas import make_title

from keyboards.reply.menu_buttoans import keyboard_1
from keyboards.inline.buttons import inline_joxa
import requests

router = Router()


@router.message(CommandStart())
async def do_start(message: types.Message):
    full_name = message.from_user.full_name
    await message.answer(f"Assalomu alaykum <b>{make_title(full_name)}</b>", parse_mode=ParseMode.HTML, reply_markup=inline_joxa)
    # await message.answer(reply_markup=inline_joxa)
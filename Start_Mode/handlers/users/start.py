from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.session.middlewares.request_logging import logger
from loader import bot
from data.config import ADMINS
from utils.extra_datas import make_title


import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
# from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

import requests
from bs4 import BeautifulSoup

router = Router()


@router.message(CommandStart())
async def do_start(message: types.Message):
    full_name = message.from_user.full_name

    sahifa = "https://nbu.uz/jismoniy-shaxslar-valyutalar-kursi"
    r = requests.get(sahifa)

    soup = BeautifulSoup(r.text, 'html.parser')
    news = soup.find_all(class_="currency_03_currency-item-price")

    await message.answer(f"Assalomu alaykum \n1 USD= {html.bold(news[0].text)} SOM\n <b>{make_title(full_name)}</b>", parse_mode=ParseMode.HTML)
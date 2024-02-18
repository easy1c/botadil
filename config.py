from aiogram import Dispatcher, Bot
from decouple import config

TOKEN = config ("TOKEN")
BOT = Bot(token=TOKEN)
dp = Dispatcher(bot=BOT)
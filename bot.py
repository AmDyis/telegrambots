from aiogram import Bot, types, Dispatcher
from aiogram.utils import executor
import os
from dotenv import load_dotenv, find_dotenv
from googletrans import Translator
from trans import *
from kb_client import *

load_dotenv(find_dotenv())

translator = Translator()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler(commands = ["start"])
async def welcome(message: types.Message):
    user_id = message.from_user.id
    await message.answer("Enter the text to translate")

@dp.message_handler()
async def echo_send(message: types.Message):
    await message.answer(transl(message.text))



executor.start_polling(dp, skip_updates=True)
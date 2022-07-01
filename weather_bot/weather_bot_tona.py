
import requests
from config import open_weather_token, telegram_bot_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


bot = Bot(token=telegram_bot_token)
dp = Dispatcher(bot)

btn_chaik = KeyboardButton("Чайковский")
btn_iz = KeyboardButton("Ижевск")
btn_msk = KeyboardButton("Москва")
btn_saint = KeyboardButton("Санкт-Петербург")
btn_votk = KeyboardButton("Воткинск")
btn_tokio = KeyboardButton("Токио")
btn_inno = KeyboardButton("Иннополис")

keyboard1 = ReplyKeyboardMarkup()
keyboard1.add(btn_chaik)
keyboard1.add(btn_iz)
keyboard1.add(btn_msk)
keyboard1.add(btn_saint)
keyboard1.add(btn_votk)
keyboard1.add(btn_tokio)
keyboard1.add(btn_inno)



@dp.message_handler(commands=["go"])
async def start_command(message: types.Message):
    await message.reply("какой город надо", reply_markup=keyboard1)

@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&lang=ru&units=metric"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        await message.reply(f"Погода в городе: {city}\nТемпература: {cur_weather}℃\n"
                            f"Влажность: {humidity}\nСкорость ветра: {wind_speed} м/c")

    except:
        await message.reply("название поправь")

if __name__ == "__main__":
    executor.start_polling(dp)
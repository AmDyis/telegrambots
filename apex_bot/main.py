import logging
import requests
import json

from aiogram import Bot, types, Dispatcher, executor
from keyboard import kb_client
API_BOT_TOKEN = "" # токен


logging.basicConfig(level=logging.INFO) # хуярит логи

bot = Bot(token = API_BOT_TOKEN) # назначение переменных
dp = Dispatcher(bot) # назначение переменных

@dp.message_handler(commands = ["start", "help"])
async def welcome(message: types.Message):
    user_id = message.from_user.id
    await message.answer("начнём", reply_markup=kb_client)

@dp.message_handler(commands = ["map"]) # commands = ["niggers", "apex"] выбор команды и ответ на нее
async def func(message: types.Message): # функция вызова (на что реакция): как реагирует
    user_id = message.from_user.id
    r = requests.get(
        f"https://api.mozambiquehe.re/maprotation?auth=1a7e41d5f67fa8a5c130a08bab583ab4"
    )
    data = r.json()
    (await message.answer("Текущая карта" + ": " + data['current']['map'] + " ещё " + data['current']['remainingTimer'] + "\n"
                            + "Следующая карта" + ": " + data['next']['map'] + "."))

@dp.message_handler(commands = ["craft"]) # commands = ["niggers", "apex"] выбор команды и ответ на нее
async def func(message: types.Message): # функция вызова (на что реакция): как реагирует
    user_id = message.from_user.id
    r = requests.get(
        f"https://api.mozambiquehe.re/crafting?auth=1a7e41d5f67fa8a5c130a08bab583ab4"
    )
    data = r.json()
    await message.answer("Ежедневный бандл" + "\n" +
                         data[0]['bundleContent'][0]['item'] + " - " + str(data[0]['bundleContent'][0]['cost']) + "\n"
                         + data[0]['bundleContent'][1]['item'] + " - " + str(data[0]['bundleContent'][1]['cost']))
    await message.answer("Еженедельный бандл" + "\n"
                         + data[1]['bundleContent'][0]['item'] + " - " + str(data[1]['bundleContent'][0]['cost']) + "\n" +
                         data[1]['bundleContent'][1]['item'] + " - " + str(data[1]['bundleContent'][1]['cost']))
@dp.message_handler(commands = ["predator"]) # commands = ["niggers", "apex"] выбор команды и ответ на нее
async def func(message: types.Message): # функция вызова (на что реакция): как реагирует
    user_id = message.from_user.id
    r = requests.get(
        f"https://api.mozambiquehe.re/predator?auth=1a7e41d5f67fa8a5c130a08bab583ab4"
    )
    data = r.json()
    kolvo_pred = data['RP']['PC']['totalMastersAndPreds'] + data['RP']['PS4']['totalMastersAndPreds'] + data['RP']['X1']['totalMastersAndPreds']
    kolvo_pred_AP = data['AP']['PC']['totalMastersAndPreds'] + data['AP']['PS4']['totalMastersAndPreds'] + data['AP']['X1']['totalMastersAndPreds']
    await message.answer("Для предатора в КБ - " + str(data['RP']['PC']['val']) + ". Всего предаторов в КБ - " + str(kolvo_pred))
    await message.answer("Для предатора в Аренах - " + str(data['AP']['PC']['val']) + ". Всего предаторов в Аренах - " + str(kolvo_pred_AP))



executor.start_polling(dp, skip_updates=True) # чтобы работало

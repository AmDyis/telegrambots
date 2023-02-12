from aiogram import Bot, types, Dispatcher, executor

b1 = types.KeyboardButton("/start")

kb_client= types.ReplyKeyboardMarkup(resize_keyboard = True)

kb_client.insert(b1)

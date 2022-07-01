from aiogram import Bot, types, Dispatcher, executor

b1 = types.KeyboardButton("/map")
b2 = types.KeyboardButton("/craft")
b3 = types.KeyboardButton("/predator")

kb_client= types.ReplyKeyboardMarkup(resize_keyboard = True)

kb_client.insert(b1).insert(b2).insert(b3)
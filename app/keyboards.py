from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup,InlineKeyboardButton



main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('Хочу угадать число').add('Угадай число').add('52 недели богатства')

guess3 = ReplyKeyboardMarkup(resize_keyboard=True)
guess3.add('стоп')

guess = ReplyKeyboardMarkup(resize_keyboard=True)
guess.add('Загадал').add('стоп')

guess1 = ReplyKeyboardMarkup(resize_keyboard=True)
guess1.add('Меньше').add('Больше').add('Угадал').add('стоп')
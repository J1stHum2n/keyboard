from aiogram import Bot, Dispatcher, executor, types
import csv, datetime
from handlers import *

API_TOKEN = '5202506538:AAFvpDtV7ReDFNd_EFYMwvPvjdxg65eZses'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard_markup.add(*(types.KeyboardButton(text) for text in array_keyboard))
    await message.answer(text="hello", reply_markup=keyboard_markup)


def statistics(user_id, command):
    data = datetime.datetime.today().strftime("%d-%m-%Y %H:%M")
    with open('data.csv', 'a', newline="") as fil:
        wr = csv.writer(fil, delimiter=';')
        wr.writerow([data, user_id, command])


if __name__ == '__main__':
    executor.start_polling(dp)

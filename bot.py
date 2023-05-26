from aiogram import Bot, Dispatcher, executor, types
from app import keyboards
import random
from dotenv import load_dotenv
import os



def botstart():

    load_dotenv()
    bot = Bot(os.getenv('TOKEN'))
    dp = Dispatcher(bot=bot)



    @dp.message_handler(commands=['start'])
    async def cmd_start(message: types.Message):
        await message.answer(f'{message.from_user.first_name}, добро пожаловать!',
                             reply_markup=keyboards.main)

    @dp.message_handler(text='Хочу угадать число')
    async def send_welcome(message: types.Message):
        global number, tries
        number = random.randint(1, 100)
        tries = 0
        await message.reply("Привет! Я загадал число от 1 до 100. Попробуй угадать его!", reply_markup=keyboards.guess3)

        @dp.message_handler(text='стоп')
        async def send_welcome(message: types.Message):
            global number
            number = 1000
            await message.reply("Игра остановлена.")



        @dp.message_handler(content_types=types.ContentType.TEXT)
        async def guess_number(message: types.Message):
            global number, tries
            if (number <= 100):
                guess = int(message.text)
                if (guess <= 100 and guess >= 0):
                    if guess < number:
                        tries += 1
                        await message.reply("Моё число больше.")
                    elif guess > number:
                        tries += 1
                        await message.reply("Моё число меньше.")
                    else:
                        tries += 1
                        await message.reply(f"Поздравляю! Ты угадал число за {tries} попыток.")
                        number = random.randint(1, 100)
                        tries = 0
                else:
                    await message.reply("Пожалуйста, отправь мне число от 1 до 100.")

    @dp.message_handler(text='Угадай число')
    async def send_welcome(message: types.Message):
        global number1, tries1, right, left
        await message.reply("Привет! Загадай число от 1 до 100.", reply_markup=keyboards.guess)
        left = 1
        right = 100
        tries1 = 0
        number1 = (left + right) // 2

        @dp.message_handler(text='стоп')
        async def send_welcome(message: types.Message):
            global right
            right = 1000
            await message.reply("Игра остановлена.", reply_markup=keyboards.main)

        @dp.message_handler(content_types=types.ContentType.TEXT)
        async def guess_number(message: types.Message):
            global number1, tries1, right, left
            number1 = (left + right) // 2


            tries1 = tries1 + 1
            answer = message.text
            if answer != 'Загадал':


                if right <= 100:
                    if answer != 'Угадал':

                        if answer == 'Больше':
                            left = number1
                            number1 = (left + right) // 2
                            await message.answer(f"Ваше число {number1}?.", reply_markup=keyboards.guess1)

                        elif answer == 'Меньше':
                            right = number1
                            number1 = (left + right) // 2
                            await message.answer(f"Ваше число {number1}?.", reply_markup=keyboards.guess1)



                    else:
                        await message.reply(f'Я угадал за {tries1} попыток!!!',reply_markup=keyboards.main)

            else:
                await message.answer(f"Ваше число {number1}?.", reply_markup=keyboards.guess1)



    @dp.message_handler(text='52 недели богатства')
    async def weeks52(message: types.Message):
        await message.answer(f'Введите начальный вклад')

        @dp.message_handler()
        async def handle_message(message: types.Message):
            start = int(message.text)

            total = start
            itog = 0
            for i in range(1, 53):
                string = f"{i} неделя {total} рублей"
                await bot.send_message(message.chat.id, string)
                itog += total
                total += start

            itogstr = f"Итого накоплено: {itog} рублей"
            await bot.send_message(message.chat.id, itogstr,reply_markup=keyboards.main)








    if __name__ == 'bot':
        executor.start_polling(dp)
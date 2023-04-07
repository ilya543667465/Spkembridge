import logging
from aiogram.dispatcher.filters import Command
from Def import *


logging.basicConfig(level=logging.INFO)
TOKEN = ('YOUR_TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(Command('start'))
async def start(message):
    await message.answer("Привет!")


async def main():
    dp.register_message_handler(odd_D192_monday, text=["Нечётная Д192 понедельник"])
    dp.register_message_handler(odd_D192_tuesday, text=["Нечётная Д192 вторник"])
    dp.register_message_handler(odd_D192_wednesday, text=["Нечётная Д192 среда"])
    dp.register_message_handler(odd_D192_thursday, text=["Нечётная Д192 четверг"])
    dp.register_message_handler(odd_D192_friday, text=["Нечётная Д192 пятница"])
    dp.register_message_handler(odd_D192_saturday, text=["Нечётная Д192 суббота"])
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

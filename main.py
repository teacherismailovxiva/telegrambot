import asyncio
from aiogram import Bot, Dispatcher,types
from aiogram.filters import Command

bot = Bot(token="8073848134:AAG-3zSq2sd93UJMV1AW-dEbRlIn60amooo")
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message:types.Message):
    await message.answer("Botga hush kelibsiz")

@dp.message(Command("user_info"))
async def info(message:types.Message):
    await message.answer(str(message))


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

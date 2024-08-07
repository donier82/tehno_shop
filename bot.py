import asyncio
import logging

from config import token

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

bot = Bot(token=token)
dp = Dispatcher()

@dp.message(Command('start'))
async def start(message:Message):
    await message.answer("hello my dear, как дела ?")
    
async def main():
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())
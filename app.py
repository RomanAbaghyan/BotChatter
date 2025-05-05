import asyncio
import os
import openai

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

from dotenv import find_dotenv, load_dotenv
from handlers.user import user_router


load_dotenv(find_dotenv())

# openai.api_key = os.getenv("OPENAI_API_KEY")
BOT_TOKEN = os.getenv("BOT_TOKEN")
HF_TOKEN = os.getenv("HF_TOKEN")

# headers = {
#     "Authorization": f"Bearer {HF_TOKEN}"
# }

# API_URL = "https://api-inference.huggingface.co/models/deepseek-ai/deepseek-coder-1.3b-instruct"
ALLOWED_UPDATES = ['message, edited_message']

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

dp.include_router(user_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

asyncio.run(main())
import asyncio

from aiogram import Bot, Dispatcher

from handlers.user import user_router
from config import settings

ALLOWED_UPDATES = ['message, edited_message']

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()

dp.include_router(user_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

asyncio.run(main())
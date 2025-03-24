import asyncio
import logging

from aiogram import Bot, Dispatcher

from app.database.models import init_db
from app.handlers.auth import auth_router
from app.handlers.base import base_router
from app.handlers.callbacks import collback_router
from app.handlers.calori_analyse import calori_analyse_router
from config import TELEGRAM_TOKEN


async def main():
    await init_db()
    bot = Bot(token=TELEGRAM_TOKEN)
    dp = Dispatcher()
    dp.include_routers(base_router, calori_analyse_router, collback_router, auth_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped")

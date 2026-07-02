import asyncio
from app.bot import dp, bot
from app.handlers import router
from app.scheduler import start_scheduler

async def main():
    dp.include_router(router)
    start_scheduler()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
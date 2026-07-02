from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta
from app.bot import bot

scheduler = AsyncIOScheduler()


def start_scheduler():
    scheduler.start()


def send_delayed(user_id, text, seconds):
    run_time = datetime.now() + timedelta(seconds=seconds)

    scheduler.add_job(
        bot.send_message,
        "date",
        run_date=run_time,
        args=[user_id, text]
    )
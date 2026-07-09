"""APScheduler setup for periodic background jobs."""
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from app.jobs.cleanup_job import run_cleanup
from app.jobs.report_job import run_report
from app.jobs.subscription_checker import check_subscriptions

scheduler = AsyncIOScheduler()


def start_scheduler() -> None:
    scheduler.add_job(check_subscriptions, "interval", hours=1, id="check_subscriptions")
    scheduler.add_job(run_cleanup, "cron", hour=3, id="cleanup")
    scheduler.add_job(run_report, "cron", day_of_week="mon", hour=9, id="weekly_report")
    scheduler.start()


def stop_scheduler() -> None:
    if scheduler.running:
        scheduler.shutdown(wait=False)

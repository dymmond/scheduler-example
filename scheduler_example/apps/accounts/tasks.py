import logging

from loguru import logger

from asyncz.triggers import IntervalTrigger
from esmerald.contrib.schedulers.asyncz.decorator import scheduler

logging.basicConfig()
logging.getLogger("esmerald").setLevel(logging.DEBUG)


@scheduler(name="collect_data", trigger=IntervalTrigger(seconds=1), max_instances=3)
def collect_market_data():
    logger.warning("Collecting market data")
    ...


@scheduler(
    name="send_email_newsletter",
    trigger=IntervalTrigger(seconds=3),
    max_instances=3,
)
def send_newsletter():
    logger.warning("sending email newsletter!")
    ...


count = 0


@scheduler(
    name="scheduler_demo",
    trigger=IntervalTrigger(seconds=3),
    max_instances=3,
)
def scheduler_demo():
    global count
    count += 1
    logger.warning(f"Scheduler running count {count}")

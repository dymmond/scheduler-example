import logging

from loguru import logger

from asyncz.contrib.esmerald.decorator import scheduler
from asyncz.triggers import IntervalTrigger

logging.basicConfig()
logging.getLogger("esmerald").setLevel(logging.DEBUG)


@scheduler(name="collect_data", trigger=IntervalTrigger(seconds=1), max_instances=3)
def collect_market_data():
    logger.error("Collecting market data")
    ...


@scheduler(
    name="send_email_newsletter",
    trigger=IntervalTrigger(seconds=3),
    max_instances=3,
)
def send_newsletter():
    logger.warning("sending email newsletter!")
    ...
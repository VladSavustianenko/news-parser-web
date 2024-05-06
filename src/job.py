import time
from threading import Thread

import schedule

from src.parser import Parser

parser = Parser()


schedule.every(1).hours.do(parser.execute)


def scheduled_job():
    while True:
        schedule.run_pending()
        time.sleep(1)


def start_job():
    job_thread = Thread(target=scheduled_job)
    job_thread.start()

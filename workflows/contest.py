import time

from scale.celery_app import app
from scale.tasks import task_keynesian_beauty_contest
from utils import get_queue


def check_queue():
    ql = int(get_queue()['messages'])
    if ql > 0:
        return ql
    else:
        # check queue again three times
        finished = True
        for i in range(3):
            time.sleep(4)
            ql = int(get_queue()['messages'])
            if ql > 0:
                finished = False
        if finished:
            return 0
        else:
            return ql
                

# run contest

ist = time.time()
res = task_keynesian_beauty_contest.delay(50_000)
time.sleep(5)

while check_queue() > 0:
    time.sleep(1)

# TODO fetch runtime from celery instead of using time.sleep
iet = time.time()
print(f"completed in {iet - ist} seconds")

import time

from scale.celery_app import app
from scale.tasks import task_keynesian_beauty_contest_group, task_keynesian_beauty_contest_chord
from utils import get_queue


def check_queue():
    """Sometimes (with concurrency=1) queue length drops to 0 in mid-flight, hence check multiple times"""
    ql = int(get_queue()['messages'])
    if ql > 0:
        return ql
    else:
        # check queue again three times
        finished = True
        for i in range(3):
            time.sleep(2)
            ql = int(get_queue()['messages'])
            if ql > 0:
                finished = False
        if finished:
            return 0
        else:
            return ql
                

# run contest

ist = time.time()
res = task_keynesian_beauty_contest_chord.delay(10_000)
# give it some time to start
time.sleep(5)
while check_queue() > 0:
    time.sleep(4)

print(res)
# TODO fetch runtime from celery instead of using time.sleep
iet = time.time()
print(f"completed in {iet - ist} seconds")

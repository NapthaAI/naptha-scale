from scale.tasks import task_keynesian_beauty_contest
import time

from scale.celery_app import app


# run contest

ist = time.time()
res = task_keynesian_beauty_contest.delay(50_000)
while len(app.control.inspect().reserved()['celery@Enricos-MacBook-Air.local']) > 0:
    time.sleep(2)
# TODO fetch runtime from celery instead of using time.sleep
iet = time.time()
print(f"completed in {iet - ist} seconds")





import asyncio
import time
import random
import logging
import math

from celery import group, chord

from scale.celery_app import app

logger = logging.getLogger(__name__)


@app.task(bind=True, acks_late=True)
def generate_random_number(self) -> str:
    """generate a random int"""
    time.sleep(1.0)
    return str(random.randint(0, 100))

# using GROUP (doesn't wait for all tasks to finish)

@app.task(bind=True, acks_late=False)
def task_keynesian_beauty_contest(self, num_agents: int) -> str:
    """Run a contest with num_agents"""
    logger.info(f"Running {num_agents} agents...")
    res = group(generate_random_number.s() for i in range(num_agents))()
    return res


# using CHORD
# Result backends that supports chords: Redis, Database, Memcached, and more.

@app.task(bind=True, acks_late=False, trail=True)
def my_foo_callback(numbers):
    return str(numbers)

@app.task(bind=True, acks_late=False, trail=True)
def task_keynesian_beauty_contest_chord(self, num_agents: int) -> str:
    """Run a contest with num_agents"""
    logger.info(f"Running {num_agents} agents...")
    callback = my_foo_callback.s()
    res = chord(generate_random_number.s() for i in range(num_agents))(callback)
    return res

import os

from celery import Celery
from dotenv import load_dotenv

load_dotenv(".env")

RMQ_USER = os.environ.get("RMQ_USER")
RMQ_PASSWORD = os.environ.get("RMQ_PASSWORD")
RMQ_HOST = "rabbitmq" if os.getenv("LAUNCH_DOCKER") == "true" else "localhost"
BROKER_URL = f"amqp://{RMQ_USER}:{RMQ_PASSWORD}@{RMQ_HOST}:5672/"
BACKEND_URL = f"rpc://{RMQ_USER}:{RMQ_PASSWORD}@{RMQ_HOST}:5672/"

# Celery client
app = Celery(
    "scale",
    broker=BROKER_URL,
    backend=BACKEND_URL,
    include=[ "scale.tasks" ],
)


if __name__ == '__main__':
    app.start()

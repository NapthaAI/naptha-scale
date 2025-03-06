# Scaling Test Bed


## Pre-requisites

- macOS
- install deps with `bash launch.sh`


## Develop

Run celery:

```
celery -A scale.celery_app  worker -l INFO --concurrency 1
```

or with auto-restart:

```
watchmedo auto-restart --directory=. --pattern='scale/*.py' --recursive -- celery -A scale.celery_app worker -l INFO --concurrency 1
```

python workflows/contest.py



## Monitoring

### Celery

In a separate terminal:

```
celery -A scale.celery_app flower
```

Visit: http://localhost:5555/workers


### RabbitMQ

```
rabbitmqctl list_queues name messages messages_ready messages_unacknowledged
```

## Clean up

```
bash stop_service.sh
```


--- 

Questions? Ping Enrico Rotundo (@enricorotundo)


import requests
import json

def call_rabbitmq_api(host, port, user, passwd):
  url = f"http://{host}:{port}/api/queues/%2F/celery"
  r = requests.get(url, auth=(user,passwd))
  return r



def get_queue():
  host = 'localhost'
  port = 15672
  user = 'monitoring'
  passwd = '2a55f70a841f18b97c3a7db939b7adc9e34a0f1b'
  res = call_rabbitmq_api(host, port, user, passwd)
  return dict(res.json())


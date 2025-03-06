from scale.tasks import run_random_agent

res = run_random_agent.delay()
print(res.get())



from scale.tasks import add, my_add


res = add.delay(2, 2)
print(res.get())

res = my_add.delay(2, 2)
print(res.get())
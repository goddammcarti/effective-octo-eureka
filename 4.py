import random

s = set()
for t in range(0, 10):
    s.add(random.randint(1, 10))
print(s)
a = int(input("Enter value from 1-9:"))
Not = False
for i in s:
    if i == a:
        Not = True
        break
print(Not)



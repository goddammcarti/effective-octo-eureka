import random
a = set(random.randint(1, 10) for _ in range(10))
b = set(random.randint(1, 10) for _ in range(10))

print(a)
print(b)

c = []
for i in a:
    if i in c:
        continue
    for j in b:
        if i == j:
            c.append(i)
            break

print("Общие элементы:", c)

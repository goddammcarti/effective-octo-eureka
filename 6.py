import random
a = set(random.randint(1, 13) for _ in range(15))
b = set(random.randint(1, 13) for _ in range(15))
print(a)
print(b)

diff = list(set(a) - set(b))
diff2 = list(set(b) - set(a))
c = diff + diff2
print("RESULT:", c)
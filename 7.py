
import random
a = set(random.randint(1, 13) for _ in range(15))
b = set(random.randint(1, 13) for _ in range(15))
print(a)
print(b)

a.difference_update(b)
print("\n result: ",a)

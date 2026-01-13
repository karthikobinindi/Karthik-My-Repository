
from functools import reduce

numbers = [4, 16, 36, 64]
total = reduce(lambda a, b: a + b, numbers)

print("Sum:", total)

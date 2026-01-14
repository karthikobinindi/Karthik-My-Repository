# Iterator
class Count:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration


# Generator
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print("Iterator Output:")
for i in Count(5):
    print(i)

print("\nGenerator Output:")
for j in fibonacci(5):
    print(j)

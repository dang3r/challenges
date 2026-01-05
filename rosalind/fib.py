import sys
import functools

data = sys.stdin.read()
n, k = list(map(int, data.split()))


@functools.lru_cache
def f(n, k):
    if n == 1 or n == 2:
        return 1
    return f(n - 1, k) + f(n - 2, k) * k


print(n, k)
print(f(n, k))
print(f(5, 3))

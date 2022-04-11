import math

A, B = map(int, input().split())

diff = math.sqrt(A ** 2 + B ** 2)

x = A / diff
y = B / diff

print(x, y)

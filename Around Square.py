from numpy import ceil, square


import math
N = int(input())

n = round(math.sqrt(N))

for i in range(1, n + 2):
  if i ** 2 > N:
    print((i - 1) ** 2)
    break

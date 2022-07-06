import math

N = int(input())

ans = 10 ** 13
for i in range(1, int(math.sqrt(N)) + 1):
  if N % i == 0:
    ans = min(ans, i + (N / i) - 2)

print(int(ans))

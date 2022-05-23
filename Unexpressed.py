import math
from collections import defaultdict

N = int(input())

d = defaultdict(int)
sum = 0
for a in range(2, int(math.sqrt(N)) + 1):
  b = 2
  while a ** b <= N:
    d[a ** b] = 1
    b += 1

sum = len(d)

ans = N - sum

print(ans)

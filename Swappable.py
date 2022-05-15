from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

d = defaultdict(int)

for i in range(N):
  d[A[i]] += 1

ans = 0
for i in range(N - 1):
  ans += (N - (i + 1)) - (d[A[i]] - 1)
  d[A[i]] -= 1


print(ans)

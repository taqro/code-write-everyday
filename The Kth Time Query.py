from collections import defaultdict

N, Q = map(int, input().split())
a = list(map(int, input().split()))
xk = [tuple(map(int, input().split())) for _ in range(Q)]

d = defaultdict(list)

for i in range(N):
  d[a[i]].append(i + 1)

for x, k in xk:
  if x in d and k <= len(d[x]):
    print(d[x][k - 1])
  else:
    print(-1)

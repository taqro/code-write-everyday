N, M = map(int, input().split())
a = [0] * N
b = [0] * N
c = [0] * M
d = [0] * M
for i in range(N):
  a[i], b[i] = map(int, input().split())

for i in range(M):
  c[i], d[i] = map(int, input().split())

ans = [0] * N

for i in range(N):
  min = 10 ** 9
  for j in range(M):
    diff = abs(a[i] - c[j]) + abs(b[i] - d[j])
    if min > diff:
      min = diff
      ans[i] = j + 1

for i in range(N):
  print(ans[i])

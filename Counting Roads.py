N, M = map(int, input().split())

a = [0] * M
b = [0] * M
for i in range(M):
  a[i], b[i] = map(int, input().split())

sum = [0] * N
for i in range(N):
  if i + 1 in a:
    sum[i] += a.count(i + 1)
  if i + 1 in b:
    sum[i] += b.count(i + 1)

for i in range(N):
  print(sum[i])

N = int(input())

a = [0] * N
for i in range(N):
  a[i] = int(input())

now = 0
b = 0

for i in range(N + 1):
  if now == 1:
    print(b)
    break
  if b >= N:
    print(-1)
    break
  b += 1
  now = a[now] - 1


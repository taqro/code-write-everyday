import math
N, D = map(int, input().split())

X = [0] * N
Y = [0] * N

for i in range(N):
  X[i], Y[i] = map(int, input().split())

ans = 0
for i in range(N):
  distance = math.sqrt(X[i] ** 2 + Y[i] ** 2)
  if distance <= D:
    ans += 1

print(ans)

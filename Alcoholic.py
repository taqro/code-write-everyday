N, X = map(int, input().split())
V = [0] * N
P = [0] * N

for i in range(N):
  V[i], P[i] = map(int, input().split())

ans = -1
sum = 0
for i in range(N):
  sum += V[i] * P[i]
  if sum > X * 100:
    ans = i + 1
    break

print(ans)

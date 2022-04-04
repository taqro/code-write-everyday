N = int(input())
T = list(map(int, input().split()))
M = int(input())
P = [0] * M
X = [0] * M
for i in range(M):
  P[i], X[i] = map(int, input().split())

ans = [0] * M
for i in range(M):
  sum = 0
  sum += X[i]
  for j in range(N):
    if j == P[i] - 1:
      continue
    else:
      sum += T[j]
  ans[i] = sum

for i in range(M):
  print(ans[i])

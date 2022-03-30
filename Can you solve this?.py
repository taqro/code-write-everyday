N, M ,C = map(int, input().split())
B = list(map(int, input().split()))
A = [[]] * N
for i in range(N):
  A[i] = list(map(int, input().split()))

ans = 0
for i in range(N):
  sum = 0
  for j in range(M):
    sum += A[i][j] * B[j]
  if sum + C > 0:
    ans += 1

print(ans)

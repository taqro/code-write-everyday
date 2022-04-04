N, T = map(int, input().split())
A = [0] * N
for i in range(N):
  A[i] = int(input())

ans = 0
for i in range(N - 1):
  if A[i + 1] - A[i] >= T:
    ans += T
  elif A[i + 1] - A[i] < T:
    ans += A[i + 1] - A[i]

ans += T
print(ans)

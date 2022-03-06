N = int(input())
A = [0] * N
B = [0] * N
for i in range(N):
  A[i], B[i] = map(int, input().split())

ans = 0
for i in range(N):
  ans += (B[i] * (B[i] + 1)) // 2 - ((A[i] - 1) * A[i] // 2)

print(ans)

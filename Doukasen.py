N = int(input())
A = [0] * N
B = [0] * N
for i in range(N):
  A[i], B[i] = map(int, input().split())

time = 0
for i in range(N):
  time += A[i] / B[i]

time /= 2

ans = 0
for i in range(N):
  if A[i] / B[i] <= time:
    ans += A[i]
    time -= A[i] / B[i]
  else:
    ans += B[i] * time
    break

print(ans)

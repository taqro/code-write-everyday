N = int(input())
A = list(map(int, input().split()))

sum = A[0]

for i in range(1, N):
  sum += A[i]
  sum %= 360
  A[i] = sum

A.sort()
ans = A[0]

for i in range(N - 1):
  if A[i + 1] - A[i] > ans:
    ans = A[i + 1] - A[i]

if 360 - A[-1] > ans:
  ans = 360 - A[-1]

print(ans)

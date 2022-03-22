N, M = map(int, input().split())
A = list(map(int, input().split()))

sum = 0
for i in range(N):
  sum += A[i]

sum_a = 0
for i in range(N):
  if A[i] >= sum / (4 * M):
    sum_a += 1
  if sum_a == M:
    break

if sum_a >= M:
  print("Yes")
else:
  print("No")

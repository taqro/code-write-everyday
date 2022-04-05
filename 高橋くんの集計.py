import math

N = int(input())
A = list(map(int, input().split()))

sum_1 = 0
sum_2 = 0
for i in range(N):
  if A[i] == 0:
    continue
  sum_1 += 1
  sum_2 += A[i]

ans = math.ceil(sum_2 / sum_1)

print(ans)

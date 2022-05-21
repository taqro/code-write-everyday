N = int(input())
A = list(map(int, input().split()))

sum_1 = 0
sum_2 = 0
for i in range(N):
  sum_1 += A[i] ** 2
  sum_2 += A[i]

ans = N * sum_1 - (sum_2) ** 2

print(ans)

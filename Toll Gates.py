N, M, X = map(int, input().split())
A = list(map(int, input().split()))

sum_1 = 0
sum_2 = 0
for i in range(M):
  if A[i] > X:
    sum_1 += 1
  elif A[i] < X:
    sum_2 += 1

ans = min(sum_1, sum_2)

print(ans)

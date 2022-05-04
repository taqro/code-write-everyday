N = int(input())
A = list(map(int, input().split()))
X = int(input())

sum_A = sum(A)

syou = X // sum_A
amari = X % sum_A

sum_B = sum_A * syou
cnt = 0
for i in range(N):
  sum_B += A[i]
  cnt += 1
  if sum_B > X:
    break

ans = (syou * N) + cnt

print(ans)

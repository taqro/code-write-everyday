N = int(input())
A = list(map(int, input().split()))

mod = 10 ** 9 + 7
ans = 0
sum_A = sum(A)

for i in range(N - 1):
  sum_A -= A[i]
  ans += (A[i] * sum_A)

ans %= mod

print(ans)

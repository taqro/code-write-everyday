N = int(input())
C = list(map(int, input().split()))

C.sort()


mod = (10 ** 9) + 7
base = C[0]

ans = base
for i in range(1, N):
  base -= 1
  ans *= base + C[i] - C[0]
  ans %= mod

print(ans)

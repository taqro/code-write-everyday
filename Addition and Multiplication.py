N = int(input())
K = int(input())

ans = 1
for i in range(N):
  if 2 * ans >= ans + K:
    ans += K
  else:
    ans *= 2

print(ans)

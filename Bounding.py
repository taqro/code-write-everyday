N, X = map(int,input().split())
L = list(map(int, input().split()))

ans = 1
D = 0
for i in range(N):
  D += L[i]
  if D == X:
    ans += i + 1
    break
  if D > X:
    ans += i
    break
  if i == N - 1 and X > D:
    ans = N + 1

print(ans)

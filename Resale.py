N = int(input())
V = list(map(int,input().split()))
C = list(map(int,input().split()))

ans = 0
for i in range(N):
  total = V[i] - C[i]
  if total > 0:
    ans += total

print(ans)

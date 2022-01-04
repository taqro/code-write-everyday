N, X = map(int, input().split())

m = [0] * N
for i in range(N):
  m[i] = int(input())

X -= sum(m)

m.sort()

ans = N
for i in range(N):
  if X >= m[i]:
    ans += X // m[i]
    X -= (X // m[i]) * m[i]
  else:
    break

print(ans)

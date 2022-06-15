N = int(input())
p = list(map(int, input().split()))

q = sorted(p)

ans = "NO"
for i in range(N):
  for j in range(i + 1, N):
    r = [*p]
    s = r[i]
    t = r[j]
    r[i] = t
    r[j] = s
    if r == q:
      ans = "YES"
      break

if p == q:
  ans = "YES"

print(ans)

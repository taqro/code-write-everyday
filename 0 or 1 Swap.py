N = int(input())
p = list(map(int, input().split()))

q = sorted(p)

ans = "No"
for i in range(N):
  for j in range(i + 1, N):
    r = [*p]
    s = r[i]
    t = r[j]
    r[i] = t
    r[j] = s
    print(r)
    if r == q:
      ans = "Yes"
      break

if p == q:
  ans = "Yes"

print(ans)

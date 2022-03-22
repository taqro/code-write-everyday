N = int(input())
p = [0] * N

for i in range(N):
  p[i] = int(input())

p.sort(reverse=True)

p[0] = p[0] // 2

ans = 0
for i in range(N):
  ans += p[i]

print(ans)

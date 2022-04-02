N, T = map(int, input().split())
c = [0] * N
t = [0] * N

for i in range(N):
  c[i], t[i] = map(int, input().split())

ans = 10 ** 9
for i in range(N):
  if T >= t[i]:
    if ans > c[i]:
      ans = c[i]

if ans == 10 ** 9:
  ans = "TLE"

print(ans)

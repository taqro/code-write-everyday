from cmath import sqrt


N = int(input())
x = [0] * N
y = [0] * N

for i in range(N):
  x[i], y[i] = map(int, input().split())

ans = 0

def tilt(a, b, c, d):
  res = (b - d) / (a - c)
  return res

for i in range(N):
  for j in range(i + 1, N):
    if tilt(x[i], y[i], x[j], y[j]) <= 1 and -1 <= tilt(x[i], y[i], x[j], y[j]):
      ans += 1

print(ans)

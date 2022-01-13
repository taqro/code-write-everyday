import math
N = int(input())

x = [0] * N
y = [0] * N
for i in range(N):
  x[i], y[i] = map(int, input().split())

max = 0

def calc_root(a, b, c, d):
  res = math.sqrt((a - c) ** 2 + (b - d) ** 2)
  return res

for i in range(N):
  for j in range(i + 1, N):
    a = calc_root(x[i], y[i], x[j], y[j])
    if max < a:
      max = a

print(max)


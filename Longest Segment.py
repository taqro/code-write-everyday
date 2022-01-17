import math

N = int(input())
x = [0] * N
y = [0] * N
for i in range(N):
  x[i], y[i] = map(int, input().split())

def calc_root(a, b, c, d):
  calc = math.sqrt((a - c) ** 2 + (b - d) ** 2)
  return calc

max = - 1
for i in range(N):
  for j in range(i + 1, N):
    res = calc_root(x[i], y[i], x[j], y[j])
    if max < res:
      max = res

print(max)

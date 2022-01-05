import math

N, D = map(int, input().split())
x = [[] * D] * N
for i in range(N):
  x[i] = list(map(int, input().split()))

def cul_root(a, b):
  A = 0
  for i in range(D):
    A += (a[i] - b[i]) ** 2
  B = math.sqrt(A)
  return B

sum = 0
min = 10 ** 5
for i in range(N):
  for j in range(i + 1, N):
    c = cul_root(x[i], x[j])
    if c.is_integer():
      sum += 1

print(sum)

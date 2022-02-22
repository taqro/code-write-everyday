N = int(input())
A = [0] * N
P = [0] * N
X = [0] * N

for i in range(N):
  A[i], P[i], X[i] = map(int, input().split())

minPrice = 10 ** 12

for i in range(N):
  if X[i] - A[i] > 0 and minPrice > P[i]:
    minPrice = P[i]

if minPrice == 10 ** 12:
  minPrice = -1

print(minPrice)


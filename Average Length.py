import math
import itertools

N = int(input())
x = [0] * N
y = [0] * N
for i in range(N):
  x[i], y[i] = map(int, input().split())

arr = []
for i in range(N):
  arr.append(i)

a = list(itertools.permutations(arr))

sum = 0
for i in range(len(a)):
  for j in range(len(a[i]) - 1):
    sum += math.sqrt((x[a[i][j]] - x[a[i][j + 1]]) ** 2 + (y[a[i][j]] - y[a[i][j + 1]]) ** 2)


ans = sum / len(a)
print(ans)

S = list(input())
N = int(input())

a = []

for i in S:
  for j in S:
    a.append(i + j)

a.sort()

print(a[N - 1])

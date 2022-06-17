from collections import defaultdict

N = int(input())
S = [""] * N
for i in range(N):
  S[i] = input()

d = defaultdict(int)

for i in range(N):
  d[S[i]] += 1

max = 0
for i in d:
  if d[i] >= max:
    max = d[i]

arr = []
for i in d:
  if d[i] == max:
    arr.append(i)

arr.sort()

for i in arr:
  print(i)

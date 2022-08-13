from collections import defaultdict

A = list(map(int, input().split()))

d = defaultdict(int)

for i in range(5):
  d[A[i]] += 1

arr = [2, 3]
for i in d.values():
  if i in arr:
    arr.remove(i)

if len(arr) == 0:
  print("Yes")
else:
  print("No")

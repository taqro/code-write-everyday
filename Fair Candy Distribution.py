from collections import defaultdict

N, K = map(int, input().split())
a = list(map(int, input().split()))

d = defaultdict(int)

b = K // N
c = K % N
if c == 0:
  for i in range(N):
    print(b)
else:
  arr = [*a]
  arr.sort()
  max_arr = arr[c - 1]

  for i in range(N):
    d[a[i]] = b
    if a[i] <= max_arr:
      d[a[i]] += 1
  if N == 1:
    print(K)
  else:
    for i in range(N):
      print(d[a[i]])

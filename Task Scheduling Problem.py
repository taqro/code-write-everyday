a = list(map(int, input().split()))

min = abs(a[0] - a[1]) + abs(a[1] - a[2])

if min > abs(a[0] - a[2]) + abs(a[2] - a[1]):
  min = abs(a[0] - a[2]) + abs(a[2] - a[1])
if min > abs(a[1] - a[2]) + abs(a[2] - a[0]):
  min = abs(a[1] - a[2]) + abs(a[2] - a[0])
if min > abs(a[1] - a[0]) + abs(a[0] - a[2]):
  min = abs(a[1] - a[2]) + abs(a[2] - a[0])
if min > abs(a[2] - a[1]) + abs(a[1] - a[0]):
  min = abs(a[2] - a[1]) + abs(a[1] - a[0])
if min > abs(a[2] - a[0]) + abs(a[0] - a[1]):
  min = abs(a[2] - a[0]) + abs(a[0] - a[1])

print(min)

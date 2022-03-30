a = []
for i in range(5):
  a.append(int(input()))

ans = 0
min_diff = 10
min_index = 10
for i in range(len(a)):
  if a[i] % 10 == 0:
    b = a[i]
  else:
    b = (a[i] // 10 + 1) * 10
    c = (a[i] // 10) * 10
    if min_diff > a[i] - c:
      min_diff = a[i] - c
  ans += b

if min_diff == 10:
  min_diff = 0
else:
  ans -= (10 - min_diff)
print(ans)

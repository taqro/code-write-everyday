a = list(map(int, input().split()))

a.sort()

ans = 0

if a[1] < a[2]:
  ans += a[2] - a[1]
  b = a[1]
  a[1] += a[2] - b
  a[0] += a[2] - b

if (a[1] - a[0]) % 2 == 0:
  ans += (a[1] - a[0]) // 2
  c = a[0]
  a[0] += a[1] - c
elif (a[1] - a[0]) % 2 != 0:
  ans += 1
  a[2] += 1
  a[1] += 1
  ans += (a[1] - a[0]) // 2

print(ans)




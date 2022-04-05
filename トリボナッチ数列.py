n = int(input())

a = [0] * n
a[0] = 0
if n == 1:
  ans = 0
elif n == 2:
  ans = 0
elif n == 3:
  ans = 1
else:
  a[1] = 0
  a[2] = 1

  ans = 0
  if n == 1:
      ans = a[0]
  elif n == 2:
      ans = a[1]
  elif n == 3:
      ans = a[2]
  else:
    for i in range(3, n):
        a[i] = (a[i - 1] + a[i - 2] + a[i - 3]) %   10007
    ans = a[n - 1]

print(ans)

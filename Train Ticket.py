a = list(input())

ans = a[0]
for i in range(1 << 3):
  sum = int(a[0])
  for j in range(3):
    if i >> j & 1:
      sum += int(a[j + 1])
      ans += "+" + a[j + 1]
    else:
      sum -= int(a[j + 1])
      ans += "-" + a[j + 1]
  if sum == 7:
    break
  else:
    ans = a[0]

print(ans + "=7")


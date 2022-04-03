s = int(input())
a = [s]
for i in range(1, 10 ** 7 + 1):
  if a[i - 1] % 2 == 0:
    a.append(a[i - 1] // 2)
  else:
    a.append(3 * a[i - 1] + 1)
  if a[i] in a[0:-1]:
    print(i + 1)
    break

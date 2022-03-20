X = int(input())

sum = 100
for i in range(1, 100000):
  sum = sum + sum // 100
  if sum >= X:
    print(i)
    break

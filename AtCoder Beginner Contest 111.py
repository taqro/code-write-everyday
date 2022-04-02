N = int(input())

ans = 0
for i in range(1, 10):
  a = str(i) + str(i) + str(i)
  b = int(a)
  if b >= N:
    print(b)
    break



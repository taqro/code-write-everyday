N = int(input())

x = 0
for i in range(1000):
  if N >= 3:
    N -= 3
    x += 1
  else:
    break

print(x)

import math

P = int(input())
cnt = 0
for i in range(10, 0, -1):
  syo = P // math.factorial(i)
  amari = P % math.factorial(i)
  if syo > 100:
    syo = 100
  cnt += syo
  P = amari
  if P == 0:
    break

print(cnt)


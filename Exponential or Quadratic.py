import math

n = int(input())

if 2 * math.log(n) < n * math.log(2):
  print("Yes")
else:
  print("No")

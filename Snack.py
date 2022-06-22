import math

A, B = map(int, input().split())

if A % B == 0:
  print(A)
elif B % A == 0:
  print(B)
else:
  print((A // math.gcd(A, B)) * B)

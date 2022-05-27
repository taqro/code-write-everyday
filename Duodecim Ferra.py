import math

L = int(input())

ans = 0
amari = L - 12

if amari == 0:
  ans = 1
else:
  ans += (math.factorial(amari + 11)) // ((math.factorial(11)) * math.factorial(amari))

print(ans)

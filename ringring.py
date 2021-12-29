a, b, c = map(int, input().split())

min = a + b
if min >= b + c:
  min = b + c

if min >= c + a:
  min = c + a


print(min)

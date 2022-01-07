import math

N = int(input())

min = 10 ** 9
for a in range(1, int(math.sqrt(N)) + 1):
  b = N / a
  if b.is_integer() == False:
    continue
  b = int(b)
  digit_a = len(str(a))
  digit_b = len(str(b))
  if min > max(digit_a, digit_b):
    min = max(digit_a, digit_b)

print(min)

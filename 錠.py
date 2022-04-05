a = int(input())
b = int(input())

sum_1 = 0
sum_2 = 0
if b > a:
  sum_1 = b - a
  sum_2 = a + (10 - b)
elif b < a:
  sum_1 = a - b
  sum_2 = b + (10 - a)

ans = min(sum_1, sum_2)

print(ans)

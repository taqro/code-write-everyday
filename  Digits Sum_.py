N = int(input())

min = 10 ** 9
def findSumDigits(x):
  sum = 0
  while x > 0:
    sum += x % 10
    x = x // 10
  return sum

for i in range(1,N // 2 + 1):
  a = i
  b = N - i
  sum = findSumDigits(a) + findSumDigits(b)
  if min > sum:
    min = sum

print(min)

N = int(input())
a = list(map(int, input().split()))

min_1 = 0
min_2 = 0
sum_1 = 0
sum_2 = 0
for i in range(N):
  sum_1 += a[i]
  sum_2 += a[i]
  if i % 2 != 0:
    if sum_1 >= 0:
      min_1 += sum_1 + 1
      sum_1 = -1
  elif i % 2 == 0:
    if sum_1 <= 0:
      min_1 += abs(sum_1) + 1
      sum_1 = 1
  if i % 2 != 0:
    if sum_2 <= 0:
      min_2 += abs(sum_2) + 1
      sum_2 = 1
  elif i % 2 == 0:
    if sum_2 >= 0:
      min_2 += sum_2 + 1
      sum_2 = -1

print(min(min_1, min_2))

A = list(map(int, input().split()))

sum_1 = 0
sum_2 = 0

for i in range(3):
  if A[i] == 5:
    sum_1 += 1
  if A[i] == 7:
    sum_2 += 1

if sum_1 == 2 and sum_2 == 1:
  print("YES")
else:
  print("NO")

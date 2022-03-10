N = list(map(int, input().split()))

sum = 0
for i in range(len(N)):
  sum += N[i]

if sum % 9 == 0:
  print("Yes")
else:
  print("No")

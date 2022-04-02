N = list(input())

sum = 0
for i in range(len(N)):
  sum += int(N[i])

if int("".join(N)) % sum == 0:
  print("Yes")
else:
  print("No")

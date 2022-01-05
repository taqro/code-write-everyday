N = int(input())

ans = 0
for i in range(26):
  flag = True
  for j in range(16):
    ans = 4 * i + 7 * j
    if ans == N:
      print("Yes")
      flag = False
      break
  if flag == False:
    break

if ans != N:
  print("No")

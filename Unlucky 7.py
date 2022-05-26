N = int(input())

ans = 0
for i in range(1, N + 1):
  oct_i = str(oct(i))[2:]
  flag = True
  for j in list(str(i)):
    if j == "7":
      flag = False
  for j in list(oct_i):
    if j == "7":
      flag = False
  if flag:
    ans += 1

print(ans)

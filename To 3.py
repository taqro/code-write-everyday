N = list(input())

ans = 100
for i in range(2 ** (len(N))):
  arr = []
  for j in range(len(N)):
    if ((i >> j) & 1):
      arr.append(N[j])
  if len(arr) != 0:
    num_arr = int("".join(arr))
    num = len(N) - len(arr)
    if num_arr % 3 == 0 and ans > num:
      ans = num

if ans == 100:
  print(-1)
else:
  print(ans)

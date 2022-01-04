N = int(input())
max = 0
max_num = 0
for i in range(1,N + 1):
  a = i
  sum = 0
  for j in range(7):
    if a % 2 == 0:
      a /= 2
      sum += 1
    else:
      break
  if max < sum:
      max = sum
      max_num = i

if N == 1:
  max_num = 1

print(max_num)

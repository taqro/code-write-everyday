n = int(input())

ans = 10 ** 9
for i in range(1,n):
  for j in range(i,n):
    if i * j > n:
      break
    diff = j - i
    res = n - (i * j)
    if ans > diff + res:
      ans = diff + res

if n == 1:
  ans = 0

print(ans)

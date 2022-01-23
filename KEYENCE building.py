
N = int(input())
S = list(map(int, input().split()))

ans = 0
for s in S:
  flag = False
  for i in range(1,301):
    for j in range(i, 301):
      if (4 * i * j + 3 * i + 3 * j) == s:
        flag = True
  if flag == False:
    ans += 1

print(ans)

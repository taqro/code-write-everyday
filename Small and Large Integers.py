A, B, K = map(int, input().split())

ans = []
if 2 * K - (B - A) > 0:
  ans = list(range(A, B + 1))
else:
  for i in range(K):
    ans.append(A + i)
  for i in range(K):
    ans.append(B - i)
  ans.sort()


for i in range(len(ans)):
  print(ans[i])

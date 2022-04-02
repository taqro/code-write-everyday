N = int(input())
W = [[]] * N
for i in range(N):
  W[i] = input()

set_W = set(W)
ans = "Yes"
if len(W) != len(set_W):
  ans = "No"

for i in range(N - 1):
  if W[i][-1] != W[i + 1][0]:
    ans = "No"
    break

print(ans)


N = int(input())
L = [[]] * N
for i in range(N):
  L[i] = list(input().split())

M = [""]* N
for i in range(N):
  M[i] = ",".join(L[i])

set_M = set(M)
ans = len(set_M)

print(ans)

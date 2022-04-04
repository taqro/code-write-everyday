N, Q = map(int, input().split())
L = [0] * Q
R = [0] * Q
T = [0] * Q
for i in range(Q):
  L[i], R[i], T[i] = map(int, input().split())

ans = [0] * (N + 1)
for i in range(Q):
  for j in range(L[i], R[i] + 1):
    ans[j] = T[i]

for i in range(1,len(ans)):
  print(ans[i])

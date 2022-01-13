N = int(input())

A = []

for i in range(N):
  A.append(int(input()))

B = {}
for i in A:
  if i in B:
    B[i] += 1
  else:
    B[i] = 1
ans = 0
for v in B.values():
  if v % 2 != 0:
    ans += 1

print(ans)






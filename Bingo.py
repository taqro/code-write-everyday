A = [[0] * 3] * 3
for i in range(3):
  A[i] = list(map(int, input().split()))

N = int(input())
b = [0] * N
for i in range(N):
  b[i] = int(input())

for i in range(N):
  for j in range(3):
    for k in range(3):
      if b[i] == A[j][k]:
        A[j][k] = 1

ans = "No"

for i in range(3):
  cnt_1 = 0
  cnt_2 = 0
  for j in range(3):
    if A[i][j] == 1:
      cnt_1 += 1
    if A[j][i] == 1:
      cnt_2 += 1
  if cnt_1 == 3 or cnt_2 ==3:
    ans = "Yes"
    break

if A[0][0] == 1 and A[1][1] == 1 and A[2][2] == 1:
  ans = "Yes"
if A[2][0] == 1 and A[1][1] == 1 and A[0][2] == 1:
  ans = "Yes"

print(ans)

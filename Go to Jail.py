N = int(input())
D = [[]] * N

for i in range(N):
  D[i] = list(map(int, input().split()))

cnt = 0
for i in range(N):
  if D[i][0] == D[i][1]:
    cnt += 1
  else:
    cnt = 0
  if cnt == 3:
    break

if cnt == 3:
  print("Yes")
else:
  print("No")

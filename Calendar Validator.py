import copy

N, M = map(int, input().split())
B = [[]] * N
for i in range(N):
  B[i] = list(map(int, input().split()))

ans = "Yes"
if B[0][0] % 7 == 0 and M > 1:
  ans = "No"
elif 8 -  B[0][0] % 7 < M :
  ans = "No"
else:
  C = [[0] * M] * N
  C[0][0] = B[0][0]
  for i in range(1, M):
    C[0][i] = C[0][i - 1] + 1

  for i in range(1, N):
    C[i] = [0] * M

  D = copy.deepcopy(C)
  for i in range(1, N):
    for j in range(M):
      C[i][j] = D[i - 1][j] + 7
      D[i][j] = D[i - 1][j] + 7

  for i in range(N):
    for j in range(M):
      if B[i][j] > (10 ** 100 - 1) * 7 + 7:
        ans = "No"
        break
      if B[i][j] != C[i][j]:
        ans = "No"
        break

print(ans)


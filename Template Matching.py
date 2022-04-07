N, M = map(int, input().split())
A = [""] * N
B = [""] * M
for i in range(N):
  A[i] = list(input())
for i in range(M):
  B[i] = list(input())

ans ="No"

for i in range(N - M + 1):
  for j in range(N - M + 1):
    if A[i][j] == B[0][0]:
      cnt = 0
      for k in range(M):
        for l in range(M):
          if A[k + i][l + j] == B[k][l]:
            cnt += 1
      if cnt == M ** 2:
        ans = "Yes"

print(ans)



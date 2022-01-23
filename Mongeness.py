H, W = map(int, input().split())

A = [[] * W] * H

for i in range(H):
  A[i] = list(map(int, input().split()))


ans = "Yes"
for i in range(H):
  for j in range(i + 1, H):
    for k in range(W):
      for l in range(k + 1, W):
        if A[i][k] + A[j][l] <= A[j][k] + A[i][l]:
          continue
        else:
          ans = "No"
          break

print(ans)

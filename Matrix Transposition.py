H, W = map(int, input().split())
A = [[]] * H

for i in range(H):
  A[i] = list(map(int, input().split()))

B = [[]] * W

for i in range(W):
  B[i] = []
  for j in range(H):
    B[i].append(str(A[j][i]))

for i in range(W):
  print(" ".join(B[i]))

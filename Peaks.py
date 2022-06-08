N, M = map(int, input().split())
H = list(map(int, input().split()))
A = [0] * M
B = [0] * M
for i in range(M):
  A[i], B[i] = map(int, input().split())

cnt = [0] * N
for i in range(M):
  if H[A[i] - 1] < H[B[i] - 1]:
    cnt[A[i] - 1] = 1
  elif H[A[i] - 1] > H[B[i] - 1]:
    cnt[B[i] - 1] = 1
  elif H[A[i] - 1] == H[B[i] - 1]:
    cnt[A[i] - 1] = 1
    cnt[B[i] - 1] = 1

ans = cnt.count(0)

print(ans)

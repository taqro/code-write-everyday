N, M, T = map(int, input().split())
A = [0] * M
B = [0] * M

for i in range(M):
  A[i], B[i] = map(int, input().split())

start = N
N -= A[0]
for i in range(M):
  if N <= 0:
    break
  if A[0] == 1:
    pass
  else:
    N += B[i] - A[i]
    N = min(start, N)
  if i != M - 1:
    N -= A[i + 1] - B[i]
  else:
    N -= T - B[i]

if N > 0:
  print("Yes")
else:
  print("No")

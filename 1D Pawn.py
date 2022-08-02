N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

for i in range(Q):
  if A[L[i] - 1] == N:
    continue
  if (A[L[i] - 1] + 1) in A:
    continue
  A[L[i] - 1] += 1

for i in range(K):
  A[i] = str(A[i])

print(" ".join(A))

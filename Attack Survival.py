N, K, Q = map(int, input().split())
A = [0] * Q
for i in range(Q):
  A[i] = int(input())

B = [Q] * N
for i in range(Q):
  B[A[i] - 1] -= 1

for i in range(N):
  if K - B[i] > 0:
    print("Yes")
  else:
    print("No")

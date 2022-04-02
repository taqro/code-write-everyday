N, M = map(int, input().split())
A = [[]] * N
B = {}
for i in range(N):
  A[i] = list(map(int, input().split()))
  B[i] = set(A[i][1::])

C = B[0]

for i in range(1, N):
  C = C & B[i]

print(len(C))

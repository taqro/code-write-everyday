N = int(input())
A = list(map(int, input().split()))

B = {}

for i in range(N):
  B[i + 1] = A[i]

C = sorted(B.items(), key = lambda x: x[1], reverse=True)

print(C[1][0])

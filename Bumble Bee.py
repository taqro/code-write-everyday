N = int(input())
A = [0] * N
for i in range(N):
  A[i] = int(input())

set_A = set(A)

ans = len(A) - len(set_A)

print(ans)



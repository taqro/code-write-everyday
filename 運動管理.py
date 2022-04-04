L, H = map(int, input().split())
N = int(input())
A = [0] * N
for i in range(N):
  A[i] = int(input())


for i in range(N):
  if H < A[i]:
    print(-1)
  elif L <= A[i] and A[i] <= H:
    print(0)
  elif A[i] < L:
    print(L - A[i])

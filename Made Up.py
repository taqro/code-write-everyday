from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

arr = []
d = defaultdict(int)
for i in range(N):
  arr.append(B[C[i] - 1])
  d[B[C[i] - 1]] += 1

ans = 0
for i in range(N):
  ans += d[A[i]]

print(ans)



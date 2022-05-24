from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

d = defaultdict(int)
for i in range(2 ** N):
  d[A[i]] = i + 1

B = [*A]
while N - 1 > 0:
  C = []
  for i in range(len(B) // 2):
    if B[2 * i] < B[2 * i + 1]:
      C.append(B[2 * i + 1])
    else:
      C.append(B[2 * i])
  B = [*C]
  N -= 1

B.sort()

print(d[B[0]])

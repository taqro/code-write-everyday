N = int(input())
A = [0] * N
B = [0] * N

for i in range(N):
  A[i], B[i] = map(int, input().split())

min_sum = 10 ** 9
min_A1 = 10 ** 9
min_B1 = 10 ** 9
min_A2 = 10 ** 9
min_B2 = 10 ** 9
min_sep = 10 ** 9
num_A = -1
num_B = -1

for i in range(i):
  min_sum = min(min_sum, A[i] + B[i])
  if min_A1 > A[i]:
    min_A1 = A[i]
    num_A = i
  if min_B2 > B[i]:
    min_B2 = B[i]
    num_B = i

for i in range(N):
  if min_B1 > B[i] and i != num_A:
    min_B1 = B[i]
  if min_A2 > A[i] and i != num_B:
    min_A2 = A[i]

min_sep = min(max(min_A1, min_B1), max(min_A2, min_B2))

ans = min(min_sum, min_sep)

print(ans)

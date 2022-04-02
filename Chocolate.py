N = int(input())
D, X = map(int, input().split())
A = [0] * N
for i in range(N):
  A[i] = int(input())

sum = 0
for i in range(N):
  for j in range(100):
    if A[i] * j + 1 > D:
      break
    else:
      sum += 1

sum += X

print(sum)

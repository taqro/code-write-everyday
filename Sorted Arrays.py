N = int(input())
A = list(map(int, input().split()))
sum = 0
i = 0
while i < N:
  while i + 1 < N and A[i] == A[i + 1]:
    i += 1
  if i + 1 < N and A[i] < A[i + 1]:
    while i + 1 < N and A[i] <= A[i + 1]:
      i += 1
  elif i + 1 < N and A[i] > A[i + 1]:
    while i + 1 < N and A[i] >= A[i + 1]:
      i += 1
  sum += 1
  i += 1
print(sum)

N = int(input())
A = [0] * N
for i in range(N):
  A[i] = int(input())

set_A = set(A)
arr_A = list(set_A)
arr_A.sort(reverse=True)

print(arr_A[1])

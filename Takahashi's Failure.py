N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

max = 0
max_list = []
for i in range(N):
  if max < A[i]:
    max = A[i]
    max_list.append(i)

max_list = []
for i in range(N):
  if max == A[i]:
    max_list.append(i)

ans = "No"
for i in range(K):
  if B[i] - 1 in max_list:
    ans = "Yes"
    break

print(ans)

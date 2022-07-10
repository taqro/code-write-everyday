N, M = map(int, input().split())
A = [0] * N
B = [0] * N
for i in range(N):
  A[i], B[i] =  map(int, input().split())

arr = []
for i in range(N):
  arr.append([A[i], B[i]])

arr.sort(key=lambda x: x[0])

sum = 0
ans = 0
for i in range(N):
  if sum + arr[i][1] < M:
    sum += arr[i][1]
    ans += arr[i][0] * arr[i][1]
  elif sum + arr[i][1] >= M:
    ans += (M - sum) * arr[i][0]
    break

print(ans)

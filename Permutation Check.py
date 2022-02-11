N = int(input())
A = list(map(int, input().split()))

A.sort()

ans = "Yes"

for i in range(N):
  if A[i] != i + 1:
    ans = "No"
    break
print(ans)

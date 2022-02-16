N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort()

ans = B[0] - A[0] + 1
if ans < 0:
  ans = 0

print(ans)

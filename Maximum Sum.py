A = list(map(int, input().split()))
K = int(input())

ans = 0
for i in range(K):
  a = A[0] * 2 + A[1] + A[2]
  b = A[0]+ A[1] * 2  + A[2]
  c = A[0]+ A[1] + A[2] * 2
  if a >= b and a >= c:
    ans = a
    A[0] *= 2
  elif b >= a and b >= c:
    ans = b
    A[1] *= 2
  elif c >= a and c >= b:
    ans = c
    A[2] *= 2

print(ans)

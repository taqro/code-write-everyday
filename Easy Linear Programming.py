A, B, C, K = map(int, input().split())

sum = 0

if A >= K:
  sum = K
  K = 0
else:
  sum = A
  K -= A

if B >= K and K != 0:
  K = 0
elif K > B and K != 0:
  K -= B

if K != 0:
  sum -= K

print(sum)

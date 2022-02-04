A = list(map(int, input()))

ans = "Strong"

if A[0] == A[1] and A[1] == A[2] and A[2] == A[3]:
  ans = "Weak"

if A[0] + 1 == A[1] and A[1] + 1 == A[2] and A[2] + 1 == A[3]:
  ans = "Weak"

if A[0] == 9 and A[1] == 0 and A[2] == 1 and A[3] == 2:
  ans = "Weak"

if A[0] == 8 and A[1] == 9 and A[2] == 0 and A[3] == 1:
  ans = "Weak"

if A[0] == 7 and A[1] == 8 and A[2] == 9 and A[3] == 0:
  ans = "Weak"

print(ans)

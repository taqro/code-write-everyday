S = list(input())
T = input()

ans = "No"

for i in range(len(S) - 1):
  U = S.copy()
  a = U[i]
  b = U[i + 1]
  U[i] = b
  U[i + 1] = a
  A = "".join(U)
  if A == T:
    ans = "Yes"
    break

if "".join(S) == T:
  ans = "Yes"

print(ans)

N, M, X, T, D = map(int, input().split())

T_0 = T - (X - 1) * D

if M >= X:
  print(T)
else:
  ans = T_0 + (M - 1) * D
  print(ans)


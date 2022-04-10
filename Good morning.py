A, B, C, D  = map(int, input().split())

if A < C:
  print("Takahashi")
elif A > C:
  print("Aoki")
elif A == C and B < D:
  print("Takahashi")
elif A == C and B > D:
  print("Aoki")
elif A == C and B == D:
  print("Takahashi")

A, B, C, D = map(int, input().split())

if B < C or D < A:
  print(0)
elif A <= C and B <= D:
  print(B - (C - A))
elif A <= C and B > D:
  print(D - C)
elif A > C and B <= D:
  print(B - A)
elif A > C and B > D:
  print(D - A)


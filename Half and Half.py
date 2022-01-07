A, B, C, X, Y = map(int, input().split())

sum = 0
if 2 * C < A + B:
  if X >= Y:
    if 2 * C < A:
      sum += (2 * C) * X
    else:
      X -= Y
      sum += (A * X) + (2 * C) * Y
  else:
    if 2 * C < B:
      sum += (2 * C) * Y
    else:
      Y -= X
      sum += (B * Y) + (2 * C) * X
else:
  sum += A * X + B * Y

print(sum)

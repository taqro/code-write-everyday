A, B = map(int, input().split())

sum = 0
if A >= B:
  sum += A
  A -= 1
else:
  sum += B
  B -= 1

if A >= B:
  sum += A
  A -= 1
else:
  sum += B
  B -= 1

print(sum)

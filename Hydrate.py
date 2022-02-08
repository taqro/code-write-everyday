A, B, C, D = map(int, input().split())

blue = A
red = 0

for i in range(10 ** 5 + 1):
  blue = A + B * i
  red = C * i
  if blue <= D * red:
    print(i)
    break
  if i == 10 ** 5:
    print(-1)
    break

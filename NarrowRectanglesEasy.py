W, a, b = map(int, input().split())

if a + W <= b:
  print(b - (a + W))
elif a + W > b and a < b:
  print(0)
elif b + W <= a:
  print(a - (b + W))
elif a == b:
  print(0)

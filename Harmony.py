A, B = map(int, input().split())

if ((A + B) / 2).is_integer():
  print((A + B) // 2)
else:
  print("IMPOSSIBLE")

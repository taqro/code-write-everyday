A, B, X = map(int, input().split())

if X < A:
  print("NO")
elif X - A <= B:
  print("YES")
else:
  print("NO")

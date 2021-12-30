X = int(input())
A = int(input())
B = int(input())

X = X - A
for i in range(1000000):
  if X - B >= 0:
    X -= B
  else:
    break

print(X)

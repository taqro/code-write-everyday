X = list(input())

for i in range(50):
  if X[-1] == "o" or X[-1] == "k" or X[-1] == "u":
    X.pop(-1)
  if len(X) > 1:
    if  X[-1] == "h" and X[-2] == "c":
      X.pop(-1)
      X.pop(-1)
  if len(X) == 0:
    break

if len(X) == 0:
  print("YES")
else:
  print("NO")

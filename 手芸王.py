N = int(input())
S = list(input())

acs = ["b"]
if N % 2 != 0:
  for i in range(1, (N - 1) // 2 + 1):
    if i % 3 == 1:
      acs.insert(0, "a")
      acs.append("c")
    elif i % 3 == 2:
      acs.insert(0, "c")
      acs.append("a")
    elif i % 3 == 0:
      acs.insert(0, "b")
      acs.append("b")

if S == acs:
  print((N - 1) // 2)
else:
  print(-1)


S = list(input())
T = int(input())

x = 0
y = 0

cnt = 0
for i in range(len(S)):
  if S[i] == "L":
    x -= 1
  elif S[i] == "R":
    x += 1
  elif S[i] == "U":
    y += 1
  elif S[i] == "D":
    y -= 1
  elif S[i] == "?":
    cnt += 1

dist = abs(x) + abs(y)

if T == 1:
  print(dist + cnt)
elif T == 2:
  if dist >= cnt:
    print(dist - cnt)
  elif dist < cnt:
    cnt -= dist
    if cnt % 2 == 0:
      print(0)
    elif cnt % 2 != 0:
      print(1)

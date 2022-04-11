N = int(input())
T = list(input())

x = 0
y = 0
now = "E"

for i in range(N):
  if T[i] == "S":
    if now == "E":
      x += 1
    elif now == "W":
      x -= 1
    elif now == "N":
      y += 1
    elif now == "S":
      y -= 1
  elif T[i] == "R":
    if now == "E":
      now = "S"
    elif now == "W":
      now = "N"
    elif now == "N":
      now = "E"
    elif now == "S":
      now = "W"

print(x, y)

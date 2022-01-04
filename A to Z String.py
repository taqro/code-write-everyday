s = input()

a = 0
z = 0
cnt = 0

for i in range(len(s)):
  if s[i] == "A" and  cnt == 0:
    a = i
    cnt = 1
  elif s[i] == "Z":
    z = i + 1

print(z - a)

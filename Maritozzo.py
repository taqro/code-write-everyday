a = input()
b = input()
c = input()
T = list(input())

ans = ""
for t in T:
  if t == "1":
    ans += a
  elif t == "2":
    ans += b
  elif t == "3":
    ans += c

print(ans)


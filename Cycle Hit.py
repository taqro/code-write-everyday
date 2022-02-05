a = input()
b = input()
c = input()
d = input()

l = ["H", "2B", "3B", "HR"]

try:
    l.remove(a)
except ValueError:
    pass
try:
    l.remove(b)
except ValueError:
    pass
try:
    l.remove(c)
except ValueError:
    pass
try:
    l.remove(d)
except ValueError:
    pass
if len(l) == 0:
  print("Yes")
else:
  print("No")

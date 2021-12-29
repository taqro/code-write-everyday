a = list(input().split())

b = a[0]
a.sort()

if a[0] == a[1]:
  print("=")
elif a[0] == b:
  print("<")
else:
  print(">")

s = list(input())
t = list(input())

s.sort()
t.sort(reverse=True)

a = [ "", ""]

for i in range(len(s)):
  a[0] += s[i]
for i in range(len(t)):
  a[1] += t[i]

b = a[0]

a.sort()

if a[0] == a[1]:
  print("No")
elif a[0] == b:
  print("Yes")
else:
  print("No")



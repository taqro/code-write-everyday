N = int(input())
s = [""] * N
for i in range(N):
  s[i] = input()

M = int(input())
t = [""] * M
for i in range(M):
  t[i] = input()

a = {}
for i in range(N):
  if s[i] not in a:
    a[s[i]] = 1
  else:
    a[s[i]] += 1

b = {}
for i in range(M):
  if t[i] not in b:
    b[t[i]] = 1
  else:
    b[t[i]] += 1

max = 0
for key in a:
  c = a[key]
  if key in b:
    c -= b[key]
  if max < c:
    max = c

print(max)

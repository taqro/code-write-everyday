A, B = map(int, input().split())

a = [A, B]
a.sort()
a[0] = str(a[0])[::-1]
a[1] = str(a[1])[::-1]

ans = "Easy"

for i in range(len(str(a[1]))):
  if len(a[0]) <= i:
    break
  if int(a[0][i]) + int(a[1][i]) >= 10:
    ans = "Hard"

print(ans)

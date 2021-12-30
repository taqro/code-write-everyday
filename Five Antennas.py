a = [0] * 6

for i in range(6):
  a[i] = int(input())

ans = "Yay!"
for i in range(5):
  if a[i + 1] - a[i] > a[5]:
    ans = ":("

if a[4] - a[0] > a[5]:
  ans = ":("

print(ans)

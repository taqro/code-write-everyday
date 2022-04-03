H, W = map(int, input().split())
a = [[]] * H
for i in range(H):
  a[i] = list(input())

for i in range(H):
  a[i].insert(0, "#")
  a[i].append("#")

a.insert(0,["#"] * (W + 2))
a.append(["#"] * (W + 2))

for i in range(H + 2):
  print("".join(a[i]))

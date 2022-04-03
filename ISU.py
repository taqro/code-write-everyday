X, Y, Z = map(int, input().split())

ans = 1
ocu = Y + 2 * Z
for i in range(1, 10 ** 5):
  ocu += Y + Z
  if X >= ocu:
    ans += 1
  else:
    break

print(ans)

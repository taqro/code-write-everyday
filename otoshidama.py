N, Y = map(int, input().split())

ans = [-1, -1, -1]
for i in range(N + 1):
  for j in range(N + 1):
    if (Y - (10000 * i + 5000 * j)) % 1000 == 0 and i + j + (Y - (10000 * i + 5000 * j)) // 1000 == N and (Y - (10000 * i + 5000 * j)) // 1000 >= 0:
      ans = [i, j, (Y - (10000 * i + 5000 * j)) // 1000]

print(str(ans[0]) + " " + str(ans[1]) + " " + str(ans[2]))

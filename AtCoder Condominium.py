N, K = map(int, input().split())

ans = 0
for i in range(1, N + 1):
  for j in range(1, K + 1):
    num_str = str(i) + "0" + str(j)
    num = int(num_str)
    ans += num

print(ans)


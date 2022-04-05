a, b = map(int, input().split())

c = b - a
sum = 0
for i in range(1, c + 1):
  sum += i

ans = sum - b
print(ans)

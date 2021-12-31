H, A = map(int, input().split())

sum = 0
for i in range(10 ** 4 + 1):
  if H > 0:
    H -= A
    sum += 1
  else:
    break

print(sum)

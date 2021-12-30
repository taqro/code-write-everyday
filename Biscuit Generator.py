A, B, T = map(int, input().split())

sum = 0
for i in range(1,21):
  if i * A <= T:
    sum += B
  else:
    break

print(sum)

A = int(input())

max = 0
for i in range(1, 100):
  for j in range(1, 100):
    if i + j == A:
      if max < i * j:
        max = i * j

print(max)

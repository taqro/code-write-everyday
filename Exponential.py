X = int(input())
ans = 0
for i in range(2,10):
  for j in range(100):
    if X >= j ** i and j ** i > ans:
      ans = j ** i

print(ans)

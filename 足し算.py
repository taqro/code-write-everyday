N = int(input())

sum = 0
ans =[]

for i in range(4, -1, -1):
  if N >= 2 ** i:
    N -= 2 ** i
    sum += 1
    ans.append(2 ** i)

print(sum)
for i in ans:
  print(i)

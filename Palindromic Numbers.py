A, B = map(int, input().split())

sum = 0
for i in range(A, B + 1):
  if str(i)[0] == str(i)[4] and str(i)[1] == str(i)[3]:
    sum += 1

print(sum)

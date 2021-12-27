a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

s = [a, b, c]

sum = 0

for i in range(3):
  sum += s[i][0] * s[i][1] * 0.1

print(int(sum))

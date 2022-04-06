N, A, B = map(int, input().split())
s = [0] * N
d = [0] * N
for i in range(N):
  s[i], d[i] = input().split()

sum = 0
for i in range(N):
  if s[i] == "East":
    if int(d[i]) < A:
      sum += A
    elif A <= int(d[i]) and int(d[i]) <= B:
      sum += int(d[i])
    elif int(d[i]) > B:
      sum += B
  elif s[i] == "West":
    if int(d[i]) < A:
      sum -= A
    elif A <= int(d[i]) and int(d[i]) <= B:
      sum -= int(d[i])
    elif int(d[i]) > B:
      sum -= B
ans = ""
if sum < 0:
  ans = "West " + str(-sum)
elif sum == 0:
  ans = "0"
elif sum > 0:
  ans = "East " + str(sum)

print(ans)

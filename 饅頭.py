A, B ,C = map(int, input().split())

sum = 0
if A >= B:
  for i in range(1000001):
    if C >= B:
      C -= B
      sum += 1
    elif C >= A:
      C -= A
      sum += 1
    else:
      break
else:
  for i in range(1000001):
    if C >= A:
      C -= A
      sum += 1
    elif C >= B:
      C -= B
      sum += 1
    else:
      break

print(sum)

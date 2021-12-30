P, Q, R = map(int, input().split())

min = P + Q

if min > Q + R:
  min = Q + R

if min > R + P:
  min = R + P

print(min)

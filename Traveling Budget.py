A = int(input())
B = int(input())
C = int(input())
D = int(input())

min = 0
if A > B:
  min += B
else:
  min += A

if C > D:
  min += D
else:
  min += C

print(min)

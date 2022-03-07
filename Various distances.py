import math

N = int(input())
x = list(map(int, input().split()))

m_D = 0
e_D = 0
t_D = 0

for i in range(N):
  m_D += abs(x[i])
  e_D += x[i] ** 2
  t_D = max(t_D, abs(x[i]))

e_D = math.sqrt(e_D)

print(m_D)
print(e_D)
print(t_D)

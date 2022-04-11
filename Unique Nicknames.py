N = int(input())
s = [""] * N
t = [""] * N
for i in range(N):
  s[i], t[i] = input().split()

u = [ *s ]
ans = "Yes"
for i in range(N):
  arr_1 = [*s[:i], *s[i + 1:]]
  arr_2 = [*t[:i], *t[i + 1:]]
  if u[i] in arr_1 or u[i] in arr_2:
    u[i] = t[i]
  if u[i] in arr_1 or u[i] in arr_2:
    ans = "No"
    break

set_u = set(u)
if len(set_u) != len(u):
  ans = "No"

print(ans)



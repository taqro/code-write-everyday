N = int(input())

h = N // 3600
m = (N % 3600) // 60
s = N % 60

def plus_zero(time):
  if len(time) == 1:
    time = "0" + time
  return time

ans = str(plus_zero(str(h))) + ":"+str(plus_zero(str(m))) + ":" + str(plus_zero(str(s)))

print(ans)

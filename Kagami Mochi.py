N = int(input())
d = [0] * N
for i in range(N):
  d[i] = int(input())

d.sort()
d_set = set(d)
d_arr = list(d_set)

print(len(d_arr))

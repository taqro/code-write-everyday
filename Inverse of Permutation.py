N = int(input())
p = list(map(int, input().split()))

q = [""] * N

for i in range(N):
  q[p[i] - 1] = str(i + 1)

print(" ".join(q))

N = int(input())
S = [""] * N
T = [0] * N

for i in range(N):
  S[i], T[i] = input().split()

T = [int(t) for t in T]

top1 = -1
top1Name = ""
top2 = -1
top2Name = ""

for i in range(N):
  if top1 < T[i]:
    top1 = T[i]
    top1Name = S[i]
  elif top2 < T[i] < top1:
    top2 = T[i]
    top2Name = S[i]

for i in range(N):
  if top1 < T[i]:
    top1 = T[i]
    top1Name = S[i]
  elif top2 < T[i] < top1:
    top2 = T[i]
    top2Name = S[i]

print(top2Name)

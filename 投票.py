N = int(input())
S = [""] * N
for i in range(N):
  S[i] = input()

dic = {}
for i in range(N):
  if S[i] in dic:
    dic[S[i]] += 1
  else:
    dic[S[i]] = 1

min = 0
ans = ""
for i in range(N):
  if dic[S[i]] > min:
    min = dic[S[i]]
    ans = S[i]

print(ans)

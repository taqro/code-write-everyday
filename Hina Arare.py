N = int(input())
S = list(input())

ans = "Three"
for i in range(N):
  if S[i] == "Y":
    ans = "Four"
    break

print(ans)

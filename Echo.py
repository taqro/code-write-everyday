N = int(input())
S = list(input())

ans = "Yes"
for i in range(N // 2):
  if S[i] != S[i + N // 2]:
    ans = "No"
    break

if N == 1 or N % 2 != 0:
  ans = "No"

print(ans)

A, B = map(int, input().split())
S = list(input())

ans = "Yes"
for i in range(len(S)):
  if i < A and S[i] == "-":
    ans = "No"
    break
  elif i == A and S[i] != "-":
    ans = "No"
    break
  elif A < i and S[i] == "-":
    ans = "No"
    break

print(ans)

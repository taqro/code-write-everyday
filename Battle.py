A, B, C, D = map(int, input().split())

ans = ""
while A > 0 and C > 0:
  C -= B
  if C <= 0:
    ans = "Yes"
    break
  A -= D
  if A <= 0:
    ans = "No"
    break

print(ans)

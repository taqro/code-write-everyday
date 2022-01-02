A, B, C = map(int, input().split())

ans = "NO"
for i in range(1,101):
  if A * i == B * ((A * i) // B) + C:
    ans = "YES"

print(ans)

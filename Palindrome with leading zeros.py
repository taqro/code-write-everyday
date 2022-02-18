N = input()

ans = "No"

for i in range(10):
  res = "0" * i + N
  if res == res[::-1]:
    ans = "Yes"

print(ans)

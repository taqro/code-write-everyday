w = list(input())
set_w  = set(w)
arr_w = list(set_w)

ans = "Yes"

for i in range(len(arr_w)):
  if w.count(arr_w[i]) % 2 != 0:
    ans = "No"

print(ans)

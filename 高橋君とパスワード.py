s = list(input())
k = int(input())

pass_list = []
for i in range(len(s) - k + 1):
  a = ""
  for j in range(k):
    a += s[i + j]
  pass_list.append(a)

set_pass_list = set(pass_list)

print(len(set_pass_list))

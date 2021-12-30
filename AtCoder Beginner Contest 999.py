n = list(input())

for i in range(3):
  if n[i] == "1":
    n[i] = "9"
  elif n[i] == "9":
    n[i] = "1"

print(int(n[0] + n[1] + n[2]))

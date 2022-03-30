S = list(input())

a = S[0] + S[1]
b = S[2] + S[3]
c = int(a)
d = int(b)

if 0 < c and c <= 12 and 0 < d and d <= 12:
  print("AMBIGUOUS")
elif 0 < c and c <= 12:
  print("MMYY")
elif 0 < d and d <= 12:
  print("YYMM")
else:
  print("NA")

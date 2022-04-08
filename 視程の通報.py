m = int(input())

if m < 100:
  print("00")
elif 100 <= m and m <= 5000:
  print(str(m // 100).zfill(2))
elif 6000 <= m and m <= 30000:
  print(m // 1000 + 50)
elif 35000 <= m and m <= 70000:
  print((((m // 1000) - 30) // 5) + 80)
elif 70000 < m:
  print(89)

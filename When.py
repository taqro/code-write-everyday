K = int(input())

if K <= 59:
  print("21:" + str(K).zfill(2))
else:
  print("22:" + str(K - 60).zfill(2))

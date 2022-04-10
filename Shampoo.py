V, A, B, C = map(int, input().split())

takahashi = [A, B, C]
turn = 0

while V > 0:
  V -= takahashi[turn]
  if V < 0:
    break
  turn += 1
  if turn == 3:
    turn = 0

if turn == 0:
  print("F")
elif turn == 1:
  print("M")
elif turn == 2:
  print("T")

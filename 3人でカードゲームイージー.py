S_A = list(input())
S_B = list(input())
S_C = list(input())

next_turn = "a"
while True :
  if next_turn == "a":
    if len(S_A) == 0:
      print("A")
      break
    next_turn = S_A.pop(0)
  elif next_turn == "b":
    if len(S_B) == 0:
      print("B")
      break
    next_turn = S_B.pop(0)
  elif next_turn == "c":
    if len(S_C) == 0:
      print("C")
      break
    next_turn = S_C.pop(0)

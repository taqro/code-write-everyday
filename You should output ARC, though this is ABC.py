R, C = map(int, input().split())
A_1 = [0, 0]
A_2 = [0, 0]

A_1[0], A_1[1] = map(int, input().split())
A_2[0], A_2[1] = map(int, input().split())

if R == 1:
  print(A_1[C- 1])
elif R == 2:
  print(A_2[C - 1])

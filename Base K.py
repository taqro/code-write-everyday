K = int(input())
A, B = input().split()

ten_A = 0
for i in range(len(A)):
  ten_A += int(A[len(A) - 1 - i]) * (K ** i)

ten_B = 0
for i in range(len(B)):
  ten_B += int(B[len(B) - 1 - i]) * (K ** i)

print(ten_A * ten_B)

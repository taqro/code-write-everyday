N = int(input())
A = []

for _ in range(N):
    a = int(input())
    A.append(a)

B = sorted(A)

for i in range(N):
    if A[i] != B[-1]:
        print(B[-1]) #maximum
    else:
        print(B[-2]) #maximum より一つ小さい値

N = int(input())
A = list(map(int, input().split()))

A.sort()
set_A = set(A)
arr_A = list(set_A)

for i in range(2002):
  if i not in arr_A:
    print(i)
    break

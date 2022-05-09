from itertools import permutations

S, K = input().split()

K = int(K)

A = set()

for i in permutations(S):
  A.add("".join(i))

arr = list(A)
arr.sort()

ans = arr[K - 1]

print(ans)

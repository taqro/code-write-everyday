n = int(input())
a = [int(x) for x in input().split()]
bridge = 0
human = 0
land = 1
cnt = sum(a) // n


for i in range(n):
    human += a[i]
    if human / land == cnt:
        human = 0
        land = 1
        pass
    else:
        bridge += 1
        land += 1

if sum(a) % n != 0:
    print(-1)
else:
    print(bridge)

from operator import itemgetter


def solve():
    N, W = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(reverse=True, key=itemgetter(0))  # Bの順序はどうでもいいので、Aの順だけでソートしたほうが速いです（keyを指定せずにソートしてもいいです）

    ans = 0
    rem = W
    for a, b in AB:
        t = min(rem, b)  # bかremの小さい方
        ans += t * a
        rem -= t
    return ans


print(solve())

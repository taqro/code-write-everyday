def main():
    import bisect

    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    B.sort()  # 二分探索するので、Bはソートしておきます

    INF = float('INF')
    ans = INF  # 正の無限大で初期化します
    for a in A:
        i = bisect.bisect_left(B, a)  # bisect_rightでもいいです
        # 配列外やB[-1]を参照するのを防ぐために、if文を使います
        if 0 <= i - 1 < M:
            b1 = B[i - 1]
            ans = min(ans, abs(a - b1))
        if 0 <= i < M:
            b2 = B[i]
            ans = min(ans, abs(a - b2))

    print(ans)


if __name__ == '__main__':
    main()

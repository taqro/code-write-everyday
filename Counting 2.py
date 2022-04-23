from bisect import bisect_left


def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()  # ソートしないと二分探索が正しく動きません
    for _ in range(Q):
        x = int(input())
        less_than_x_count = bisect_left(A, x)
        print(N - less_than_x_count)


main()

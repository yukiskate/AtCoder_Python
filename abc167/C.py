N, M, X = map(int, input().split())
books = [list(map(int, input().split())) for _ in range(N)]

default = 10 ** 5 * 12 + 1
min_money = default

for bits in range(1 << N):
    money = 0
    algo = [0] * M
    for i in range(N):
        if bits >> i & 1 == 1:
            money += books[i][0]
            for j in range(M):
                algo[j] += books[i][j + 1]

    if min(algo) >= X:
        min_money = min(min_money, money)

print('-1' if min_money == default else min_money)

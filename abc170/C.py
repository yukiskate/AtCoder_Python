X, N = map(int, input().split())
p = list(map(int, input().split()))

for i in range(1, 101):
    if N == 0:
        print(X)
        break
    elif p.count(X) == 0:
        print(X)
        break
    elif p.count(X-i) == 0:
        print(abs(X-i))
        break
    elif p.count(X+i) == 0:
        print(abs(X+i))
        break

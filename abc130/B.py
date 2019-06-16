N, X = map(int, input().split())
L = list(map(int, input().split()))

cnt = 1
x = 0

for v in L:
    x += v

    if x <= X:
        cnt += 1
    else:
        break

print(cnt)

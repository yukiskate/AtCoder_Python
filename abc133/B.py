import math

N, D = map(int, input().split())

tmp = []

for _ in range(N):
    x = list(map(int, input().split()))
    tmp.append(x)

cnt = 0

for i in range(len(tmp)):
    for j in range(len(tmp))[i+1:]:
        y = 0
        for k in range(D):
            y += abs(tmp[i][k] - tmp[j][k]) ** 2


        if math.sqrt(y).is_integer():
            cnt += 1

print(cnt)

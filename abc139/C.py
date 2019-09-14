N = int(input())
H = list(map(int, input().split()))

cnt = 0
tmp = 0

for i in range(N-1):

    if H[i] >= H[i+1]:
        tmp += 1
    else:
        if cnt < tmp:
            cnt = tmp

        tmp = 0

if cnt < tmp:
    cnt = tmp

print(cnt)

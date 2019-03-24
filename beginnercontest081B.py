n = map(int, input())
list = list(map(int, input().split()))

a = []

for row in list:
    cnt = 0
    while row % 2 == 0:
        row = row / 2
        cnt += 1

    a.append(cnt)

print(min(a))
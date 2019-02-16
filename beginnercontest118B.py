n = list(map(int, input().split()))

list = [list(map(int, input().split())) for i in range(n[0])]

a = {}
for i in list:
    for j in i[1:]:
        if j in a:
            a[j] = a[j] + 1
        else:
            a[j] = 1

cnt = 0
for x in a.values():
    if x == n[0]:
        cnt += 1

print(cnt)

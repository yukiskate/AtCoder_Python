n = list(map(int, input().split()))

list = [list(input().split()) for i in range(n[0])]

yen = 0
btc = 380000
for row in list:
    if row[1] == 'JPY':
        yen += int(row[0])
    else:
        yen += float(row[0]) * btc

print(yen)
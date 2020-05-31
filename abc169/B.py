N = int(input())
A = list(map(int, input().split()))

x = 1000000000000000000
res = 1

A.sort(reverse=True)

if A.count(0) > 0:
    print('0')
    exit()

for val in A:
    res = res * val
    if res > x:
        print('-1')
        break
else:
    print(res)

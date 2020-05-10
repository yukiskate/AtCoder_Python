import sys

A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
A3 = list(map(int, input().split()))
N = int(input())
index_A1 = -1
index_A2 = -1
index_A3 = -1
result_A1 = [0, 0, 0]
result_A2 = [0, 0, 0]
result_A3 = [0, 0, 0]

for i in range(N):
    b = int(input())
    try:
        index_A1 = A1.index(b)
        if index_A1 > -1:
            result_A1[index_A1] = 1
    except ValueError:
        index_A1 = -1

    try:
        index_A2 = A2.index(b)
        if index_A2 > -1:
            result_A2[index_A2] = 1
    except ValueError:
        index_A2 = -1

    try:
        index_A3 = A3.index(b)
        if index_A3 > -1:
            result_A3[index_A3] = 1
    except ValueError:
        index_A3 = -1

if sum(result_A1) == 3 or sum(result_A2) == 3 or sum(result_A3) == 3:
    print('Yes')
    sys.exit()

for i in range(3):
    if result_A1[i] + result_A2[i] + result_A3[i] == 3:
        print('Yes')
        sys.exit()

if result_A1[0] + result_A2[1] + result_A3[2] == 3:
    print('Yes')
    sys.exit()

if result_A3[0] + result_A2[1] + result_A1[2] == 3:
    print('Yes')
    sys.exit()

print('No')

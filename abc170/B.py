X, Y = map(int, input().split())

max = X * 4

if Y > max:
    print('No')
elif Y % 2 != 0:
    print('No')
else:
    for i in range(2*X, 4*X+1, 2):
        if i == Y:
            print('Yes')
            break
    else:
        print('No')

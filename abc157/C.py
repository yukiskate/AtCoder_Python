import sys

N, M = map(int, input().split())

x = []
y = []
z = []

for i in range(M):
    s1, c1 = map(int, input().split())
    if s1 == 1:
        x.append(c1)
    elif s1 == 2:
        y.append(c1)
    elif s1 == 3:
        z.append(c1)

if N == 1:
    if len(set(x)) > 1:
        print('-1')
        sys.exit()

    if len(x) == 0:
        x.append(0)

    print(str(x[0]))
    sys.exit()

elif N == 2:
    if len(x) == 0:
        x.append(1)

    if len(set(x)) > 1 or len(set(y)) > 1:
        print('-1')
        sys.exit()

    if len(y) == 0:
        y.append(0)

    if x[0] == 0 and len(x) == 1:
        print('-1')
        sys.exit()
    elif x[0] == 0 and len(x) > 1:
        print(str(x[1]) + str(y[0]))
        sys.exit()

    print(str(x[0]) + str(y[0]))
    sys.exit()

elif N == 3:
    if len(x) == 0:
        x.append(1)

    if len(set(x)) > 1 or len(set(y)) > 1 or len(set(z)) > 1:
        print('-1')
        sys.exit()

    if len(y) == 0:
        y.append(0)
    if len(z) == 0:
        z.append(0)

    if x[0] == 0 and len(x) == 1:
        print('-1')
        sys.exit()
    elif x[0] == 0 and len(x) > 1:
        print(str(x[1]) + str(y[0]) + str(z[0]))
        sys.exit()

    print(str(x[0]) + str(y[0]) + str(z[0]))
    sys.exit()

print('-1')

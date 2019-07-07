L, R = map(int, input().split())

x = 2020

if R - L > 2019:
    print(0)

else:
    for i in range(R+1)[L:]:
        for j in range(R+1)[i+1:]:

            mod = i * j % 2019

            x = min(mod, x)

    print(x)


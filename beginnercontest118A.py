list = list(map(int, input().split()))
if (list[1] % list[0] == 0):
    print(list[1] + list[0])
else:
    print(list[1] - list[0])

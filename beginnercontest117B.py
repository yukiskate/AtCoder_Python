N = input()
list = list(map(int, input().split()))

new_list = sorted(list, reverse=True)

if new_list[0] < sum(new_list[1:]):
    print('Yes')
else:
    print('No')
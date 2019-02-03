N = input()
list = list(map(int, input().split()))

new_list = sorted(list, reverse=True)

x = 0
for i in new_list[1:len(new_list)]:
    x += i

if new_list[0] < x:
    print('Yes')
else:
    print('No')
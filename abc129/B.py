N = int(input())
W = list(map(int, input().split()))

sum = sum(W)

x = 0
tmp = 0
ans = sum

for val in W:
    x = x + val
    tmp = abs((sum - x) - x)

    if ans < tmp:
        break
    else:
        ans = (sum - x) - x

print(abs(ans))

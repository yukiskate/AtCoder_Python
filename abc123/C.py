import math

n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

list = [a, b, c, d, e]

cnt = 4
min = min(list)

x = n / min

print(cnt + math.ceil(x))
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

list = [a, b, c, d, e]

n = 10
x = []

for row in list:
    x.append((row + (n - row % n) % n) - row)

x.sort()

print(sum(x[:4]) + a + b + c + d + e)


A, B = map(int, input().split())

k = A

if B == 1:
    i = 0
else:
    i = 1

while k < B:
    k = k + A - 1
    i += 1

print(i)

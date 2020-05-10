import math

N = int(input())
X = list(map(int, input().split()))

min = 0
avg = round(sum(X) / len(X))

for x in X:
    min += (x - avg)**2

print(min)

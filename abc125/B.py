N = int(input())

V = list(map(int, input().split()))
C = list(map(int, input().split()))

vsum = 0
csum = 0

for v, c in zip(V, C):
    if v - c > 0:
        vsum += v
        csum += c

print(vsum - csum)
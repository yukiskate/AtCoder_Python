N = int(input())
v = list(map(int, input().split()))

v.sort()

sum = 0

for i in range(1, N):
    sum = (v[i] + v[i-1]) / 2
    v[i] = sum

print(sum)

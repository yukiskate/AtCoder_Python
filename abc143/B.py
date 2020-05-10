N = int(input())
d = list(map(int, input().split()))

sum = 0

for i in range(N):
    for x in d[i+1:]:
       sum += d[i] * x

print(sum)

N = int(input())
B = list(map(int, input().split()))

list = []
list.append(B[0])

for i in range(1, N-1):
    list.append(min(B[i-1], B[i]))

list.append(B[N-2])

print(sum(list))

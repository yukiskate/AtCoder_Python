N = int(input())
A = list(map(int, input().split()))

arr = [0] * N

for i in A:
    arr[i-1] += 1

print(*arr, sep='\n')

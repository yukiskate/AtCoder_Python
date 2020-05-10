N = int(input())
B = list(map(int, input().split()))

arr = [0]*N

for i in range(N):
    arr[B[i]-1] = i+1

print(*arr)


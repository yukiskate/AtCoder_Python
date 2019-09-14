N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

sum = 0
bf = -1

for i in A:
    sum += B[i-1]

    if i == bf + 1:
        sum += C[i-2]

    bf = i

print(sum)

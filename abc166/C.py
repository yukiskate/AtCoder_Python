N, M = map(int, input().split())
H = list(map(int, input().split()))

result = [1] * N

for i in range(M):
    A, B = list(map(int, input().split()))
    if H[A-1] <= H[B-1]:
        result[A-1] = 0
    if H[B-1] <= H[A-1]:
        result[B-1] = 0

print(sum(result))


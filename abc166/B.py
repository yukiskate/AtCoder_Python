N, K = map(int, input().split())

result = [0] * N

for i in range(K):
    d = int(input())
    A = list(map(int, input().split()))
    for a in A:
        result[a-1] = 1
cnt = 0
for val in result:
    if val == 0:
        cnt += 1

print(cnt)

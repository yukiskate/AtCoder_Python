N, M, C = map(int, input().split())

B = list(map(int, input().split()))

A = []
for _ in range(N):
    temp = list(map(int, input().split()))
    A.append(temp)

cnt = 0
for a_list in A:
    sum = 0
    for a, b in zip(a_list, B):
        sum += a*b
    if sum + C > 0:
        cnt += 1

print(cnt)
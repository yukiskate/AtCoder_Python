N, L = map(int, input().split())

sum = 0

if L >= 0:
    for i in range(1, N):
        sum += int(i) + L

elif abs(L) < N:
    for i in range(N):
        sum += int(i) + L

else:
    for i in range(0, N-1):
        sum += int(i) + L

print(sum)

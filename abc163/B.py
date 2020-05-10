N, M = map(int, input().split())
A = list(map(int, input().split()))

sum_A = sum(A)

if N < sum_A:
    print('-1')
else:
    print(N - sum_A)

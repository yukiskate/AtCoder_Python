N, M = input().split()
A = list(map(int, input().split()))

arr_sum = sum(A)
A.sort(reverse=True)

min = arr_sum * (1 / (4 * int(M)))

for x in A[:int(M)]:
    if x < min:
        print('No')
        break
else:
    print('Yes')

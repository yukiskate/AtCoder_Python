import bisect

N = int(input())
L = list(map(int, input().split()))

L.sort()

ans = 0


for i in range(N-2):
    for j in range(i+1, N-1):
        ans += bisect.bisect_left(L, L[i] + L[j]) - j - 1


'''
def binary_search(key):
    left = 0
    right = N

    while left < right:

        mid = int((left + right) / 2)

        if key == L[mid]:
            return mid
        elif key > L[mid]:
            left = mid + 1
        elif key < L[mid]:
            right = mid

    return 0


for i in range(N-2):
    for j in range(i+1, N-1):
        key = L[i] + L[j]
        result = binary_search(key)
        if result != 0:
            ans += result - j - 1
'''

print(ans)

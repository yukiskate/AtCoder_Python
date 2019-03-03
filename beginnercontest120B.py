a, b, k = map(int, input().split())

array1 = []
array2 = []

array1 = [i for i in range(1, a+1) if a % i == 0]
array2 = [i for i in range(1, b+1) if b % i == 0]

array = list(set(array1) & set(array2))
array.sort()
print(array[-k])
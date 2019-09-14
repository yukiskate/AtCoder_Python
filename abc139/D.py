N = int(input())
list = range(N+1)

sum = 0
sort = sorted(list, reverse=True)
print(sort)

if N % 2 == 0:
    for i in range((int((N/2))-1)):
        sum += sort[i]
    sum += N / 2
else:
    for i in range((int((N/2))-1)):
        sum += sort[i]

print(int(sum))
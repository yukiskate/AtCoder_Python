N, M = map(int, input().split())

temp_list = []
for _ in range(N):
    temp = list(map(int, input().split()))
    temp_list.append(temp)

sort_after = sorted(temp_list, key=lambda x: x[0])

yen_min = 0
for yen, honsu in sort_after:
    if M - honsu > 0:
        yen_min += yen * honsu
        M -= honsu
    else:
        yen_min += M * yen
        break

print(yen_min)

def diff(tmp):
    if tmp > cnt:
        return tmp
    else:
        return cnt

list = list(input())

cnt = 0
tmp = 0
for row in list:
    if row in ('ACGT'):
        tmp += 1
        cnt = diff(tmp)
    else:
        cnt = diff(tmp)
        tmp = 0

print(cnt)

S = str(input())

tmp = ''
s = 'Good'

for v in S:
    if tmp == v:
        s = 'Bad'

    tmp = v

print(s)

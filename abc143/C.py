N = int(input())
S = input()

bf = ''
cnt = 0

for i in S:
    if bf != i:
        cnt += 1
        bf = i

print(cnt)

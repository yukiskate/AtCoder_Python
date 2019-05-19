N, K = map(int, input().split())
S = input()

s = ''

for i in range(len(S)):
    if i + 1 == K:
        s += S[i].lower()
    else:
        s += S[i]

print(s)


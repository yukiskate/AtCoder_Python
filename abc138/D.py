import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

N, Q = map(int, input().split())

T = [[] for i in range(N)]

for i in range(N-1):
    a, b = map(int, input().split())
    T[a-1].append(b-1)
    T[b-1].append(a-1)

ans = [0 for i in range(N)]

for i in range(Q):
    p, x = map(int, input().split())
    ans[p-1] += x

def dfs(n, r):
    for i in T[n]:
        if i != r:
            ans[i] += ans[n]
            dfs(i, n)

dfs(0, -1)

print(*ans)

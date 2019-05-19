N, K = map(int,input().split())

a = 0

for i in range(N):
  j = N - i
  b = 1

  while j < K:
      b /= 2
      j *= 2

  a += b

print(a / N)

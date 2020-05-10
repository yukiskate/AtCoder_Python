a, b, x = map(int,input().split())

min = 0
max = 10**9+1

while max - min > 1:
  mid = (max + min) // 2
  v = a * mid + b * len(str(mid))

  if v <= x:
    min = mid
  else:
    max = mid

print(min)
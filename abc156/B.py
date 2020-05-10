def Base_10_to_n(X, n):
    X_dumy = X
    out = ''
    while X_dumy>0:
        out = str(X_dumy%n) + out
        X_dumy = int(X_dumy / n)
    return out

N, K = list(map(int, input().split()))

print(len(Base_10_to_n(N, K)))

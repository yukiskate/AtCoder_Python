from fractions import Fraction

N = int(input())
A = list(map(int, input().split()))

sum = 0

for a in A:
    sum += Fraction(1, a)

print(float(1/sum))

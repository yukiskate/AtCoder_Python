from fractions import gcd

A, B, C, D = map(int, input().split())

E = C * D // gcd(C, D)

print((B-(A-1))-(B//C-(A-1)//C)-(B//D-(A-1)//D)+(B//E-(A-1)//E))

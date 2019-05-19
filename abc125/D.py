N = input()
A = list(map(int, input().split()))

i = 0
for j in range(N):
    if A[j] < 0 and (j==0 or S[j-1] == "1"):
        K -= 1
    if (K<0):
        if(S[i]=="0" and S[i+1] == "1"):
            K += 1
        i+=1

print(N-i)

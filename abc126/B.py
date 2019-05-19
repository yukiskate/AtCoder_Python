S = input()

x = int(S[:2])
y = int(S[2:])

flg1 = False
flg2 = False

if x >= 1 and x <= 12:
    flg1 = True

if y >= 1 and y <= 12:
    flg2 = True

if flg1 == True and flg2 == True:
    print('AMBIGUOUS')

elif flg1 == False and flg2 == True:
    print('YYMM')

elif flg1 == True and flg2 == False:
    print('MMYY')

else:
    print('NA')

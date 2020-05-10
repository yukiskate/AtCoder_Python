card = list(map(int, input().split()))

if card[3] > card[0] + card[1]:
    x = card[3] - card[0] - card[1]
    print(card[0] + x * -1)
else:
    if card[0] <= card[3]:
        print(card[0])
    else:
        print(card[3])

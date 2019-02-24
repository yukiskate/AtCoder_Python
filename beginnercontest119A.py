from datetime import datetime

date = input()

if datetime.strptime(date, '%Y/%m/%d') <= datetime(2019, 4, 30):
    print('Heisei')
else:
    print('TBD')

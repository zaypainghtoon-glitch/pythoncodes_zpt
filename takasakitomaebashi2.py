#takasaki to maebashi again
#18/05/2026
while True:
    timetable = {
        5: [(25,39)],

        6: [(10,23), (26,40), (38,52), (53,67)],

        7: [(3,17), (17,33), (39,53), (52,66)],

        8: [(7,21), (18,33), (36,50)],

        9: [(6,22), (28,45), (43,57)],

        10: [(7,21), (37,51)],

        11: [(10,23), (37,51)],

        12: [(14,28), (37,51)],

        13: [(9,22), (37,51)],

        14: [(7,21), (37,50)],

        15: [(8,22), (28,42), (43,58)],

        16: [(7,21), (28,43), (58,72)],

        17: [(22,36), (37,51), (57,73)],

        18: [(17,31), (36,52)],

        19: [(6,21), (31,44), (44,58)],

        20: [(1,15), (11,28), (39,53)],

        21: [(5,19), (16,31), (42,56), (55,73)],

        22: [(16,31), (33,47), (52,66)],

        23: [(17,31), (45,59)],

        24: [(6,20)]
    }


    while True:
        current=int(input('Enter current hour \nEnter like (13,14) for pm and 24 for midnight hours: '))

        if current not in timetable:
            print('Invalid hour')
            continue
        trains=timetable[current]
        print(f'\n{current}:00 trains')

        for i,train in enumerate(trains,start=1):

            depart=train[0]
            arrive=train[1]

            arriveHour=current
            arriveMin=arrive

            if arriveMin>=60:
                arriveHour+=1
                arriveMin-=60

            print(
            f'{i}. '
            f'{current}:{depart:02} '
            f'-> '
            f'{arriveHour}:{arriveMin:02}'
        )
        
# gacha system

import random

pity = 0

while True:

    p = int(input('Enter 1 to do a single pull or\nEnter 2 to do ten pulls: '))

    # 10 pulls
    if p == 2:

        for i in range(10):

            r = random.randint(1, 100)

            if r < 2:
                print('5*****')
                pity=0

            elif r >= 2 and r < 7:
                print('4**')

            else:
                print('3')

        pity = pity + 10

        print(f'Pity = {pity}')

        if pity>=90:
            print('5*****')
            pity=0

        # 1 pulls
    elif p == 1:

        for i in range(1):

            r = random.randint(1, 100)

            if r < 2:
                print('5*****')
                pity=0

            elif r >= 2 and r < 7:
                print('4**')

            else:
                print('3')

        pity = pity + 1

        print(f'Pity = {pity}')

        if pity>=90:
            print('5*****')
            pity=0
    else:
        break
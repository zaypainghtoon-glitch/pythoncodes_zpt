#両毛線　高崎から前橋駅までの時刻表
#18/05/2026
while True:
    current=int(input('Enter current hour \nEnter like (13,14) for pm and 24 for midnight hours: '))

    if current>=5 and current<=24:
        #5時
        if current==5:
            
            print('5:25->5:39')
        #6時
        elif current==6:
            roku=[10,26,38,53]
            print(f' 6:{roku[0]}, 6:{roku[1]}, 6:{roku[2]}, 6:{roku[3]}')
            choice=int(input('\nご利用する列車を１～４の中からお選びください。'))
            if choice>=1 and choice<=4:
                rokuArrive=[23,40,52,7]
                if choice==1:
                    print(f'6:{roku[0]}->6:{rokuArrive[0]}')
                elif choice==2:
                    print(f'6:{roku[1]}->6:{rokuArrive[1]}')
                elif choice==3:
                    print(f'6:{roku[2]}->6:{rokuArrive[2]}')
                elif choice==4:
                    print(f'6:{roku[3]}->7:0{rokuArrive[3]}')
                else:
                    print('\nEnter a valid number')
                    continue
            #7時
        elif current==7:
                nana=[3,17,39,52]
                print(f' 7:0{nana[0]}, 7:{nana[1]}, 7:{nana[2]}, 7:{nana[3]}')
                choice=int(input('\nご利用する列車を１～４の中からお選びください。'))
                if choice>=1 and choice<=4:
                    nanaArrive=[17,33,53,6]
                    if choice==1:
                        print(f'7:0{nana[0]}->7:{nanaArrive[0]}')
                    elif choice==2:
                        print(f'7:{nana[1]}->7:{nanaArrive[1]}')
                    elif choice==3:
                        print(f'7:{nana[2]}->7:{nanaArrive[2]}')
                    elif choice==4:
                        print(f'7:{nana[3]}->8:0{nanaArrive[3]}')
                else:
                        print('\nEnter a valid number')
                        continue
            #8時
        elif current==8:
                hachi=[7,18,36]
                print(f' 8:{hachi[0]}, 8:{hachi[1]}, 8:{hachi[2]}')
                choice=int(input('\nご利用する列車を１～３の中からお選びください。'))
                if choice>=1 and choice<=3:
                    hachiArrive=[21,33,50]
                    if choice==1:
                        print(f'8:0{hachi[0]}->8:{hachiArrive[0]}')
                    elif choice==2:
                        print(f'8:{hachi[1]}->8:{hachiArrive[1]}')
                    elif choice==3:
                        print(f'8:{hachi[2]}->8:{hachiArrive[2]}')
                    
                else:
                        print('\nEnter a valid number')
                        continue
            #9時
        elif current==9:
                kyuu=[6,28,43]
                print(f' 9:0{kyuu[0]}, 9:{kyuu[1]}, 9:{kyuu[2]}')
                choice=int(input('\nご利用する列車を１～３の中からお選びください。'))
                if choice>=1 and choice<=3:
                    kyuuArrive=[22,45,57]
                    if choice==1:
                        print(f'9:0{kyuu[0]}->9:{kyuuArrive[0]}')
                    elif choice==2:
                        print(f'9:{kyuu[1]}->9:{kyuuArrive[1]}')
                    elif choice==3:
                        print(f'9:{kyuu[2]}->9:{kyuuArrive[2]}')
                    
                else:
                        print('\nEnter a valid number')
                        continue
            #10時
        elif current==10:
                jyuu=[7,37]
                print(f' 10:0{jyuu[0]}, 10:{jyuu[1]}')
                choice=int(input('\nご利用する列車を１～２の中からお選びください。\n'))
                if choice>=1 and choice<=2:
                    jyuuArrive=[21,51]
                    if choice==1:
                        print(f'10:0{jyuu[0]}->10:{jyuuArrive[0]}')
                    elif choice==2:
                        print(f'10:{jyuu[1]}->10:{jyuuArrive[1]}')
                    
                    
                else:
                        print('\nEnter a valid number')
                        continue
            #11時
        elif current==11:
                jichi=[10,37]
                print(f' 11:{jichi[0]}, 11:{jichi[1]}')
                choice=int(input('\nご利用する列車を１～２の中からお選びください。'))
                if choice>=1 and choice<=2:
                    jichiArrive=[23,51]
                    if choice==1:
                        print(f'11:{jichi[0]}->11:{jichiArrive[0]}')
                    elif choice==2:
                        print(f'11:{jichi[1]}->11:{jichiArrive[1]}')
                    
                    
                else:
                        print('\nEnter a valid number')
                        continue
            #12時
        elif current==12:
                jni=[14,37]
                print(f' 12:{jni[0]}, 12:{jni[1]}')
                choice=int(input('\nご利用する列車を１～２の中からお選びください。'))
                if choice>=1 and choice<=2:
                    jniArrive=[28,51]
                    if choice==1:
                        print(f'12:{jni[0]}->12:{jniArrive[0]}')
                    elif choice==2:
                        print(f'12:{jni[1]}->12:{jniArrive[1]}')
                    
                    
                else:
                        print('\nEnter a valid number')
                        continue
            #13時
        elif current==13:
                jsan=[9,37]
                print(f' 13:0{jsan[0]}, 13:{jsan[1]}')
                choice=int(input('\nご利用する列車を１～２の中からお選びください。'))
                if choice>=1 and choice<=2:
                    jsanArrive=[22,51]
                    if choice==1:
                        print(f'13:0{jsan[0]}->13:{jsanArrive[0]}')
                    elif choice==2:
                        print(f'13:{jsan[1]}->13:{jsanArrive[1]}')
                    
                    
                else:
                        print('\nEnter a valid number')
                        continue
            #14時
        elif current==14:
                jyon=[7,37]
                print(f' 14:0{jyon[0]}, 14:{jyon[1]}')
                choice=int(input('\nご利用する列車を１～２の中からお選びください。'))
                if choice>=1 and choice<=2:
                    jyonArrive=[21,50]
                    if choice==1:
                        print(f'14:{jyon[0]}->14:{jyonArrive[0]}')
                    elif choice==2:
                        print(f'14:{jyon[1]}->14:{jyonArrive[1]}')
                    
                    
                else:
                        print('\nEnter a valid number')
                        continue
            #15時
        elif current==15:
                jgo=[8,28,43]
                print(f' 15:0{jgo[0]}, 15:{jgo[1]}, 15:{jgo[2]}')
                choice=int(input('\nご利用する列車を１～３の中からお選びください。'))
                if choice>=1 and choice<=3:
                    jgoArrive=[22,42,58]
                    if choice==1:
                        print(f'15:0{jgo[0]}->15:{jgoArrive[0]}')
                    elif choice==2:
                        print(f'15:{jgo[1]}->15:{jgoArrive[1]}')
                    elif choice==3:
                        print(f'15:{jgo[2]}->15:{jgoArrive[2]}')
                    
                    
                else:
                        print('\nEnter a valid number')
                        continue
            #16時
        elif current==16:
                jroku=[7,28,58]
                print(f' 16:0{jroku[0]}, 16:{jroku[1]}, 16:{jroku[2]}')
                choice=int(input('\nご利用する列車を１～３の中からお選びください。'))
                if choice>=1 and choice<=3:
                    jrokuArrive=[21,43,12]
                    if choice==1:
                        print(f'16:0{jroku[0]}->16:{jrokuArrive[0]}')
                    elif choice==2:
                        print(f'16:{jroku[1]}->16:{jrokuArrive[1]}')
                    elif choice==3:
                        print(f'16:{jroku[2]}->17:{jrokuArrive[2]}')
                    
                    
                else:
                        print('\nEnter a valid number')
                        continue
            #17時
        elif current==17:
                jnana=[22,37,57]
                print(f' 17:{jnana[0]}, 17:{jnana[1]}, 17:{jnana[2]}')
                choice=int(input('\nご利用する列車を１～３の中からお選びください。'))
                if choice>=1 and choice<=3:
                    jnanaArrive=[36,51,13]
                    if choice==1:
                        print(f'17:{jnana[0]}->17:{jnanaArrive[0]}')
                    elif choice==2:
                        print(f'17:{jnana[1]}->17:{jnanaArrive[1]}')
                    elif choice==3:
                        print(f'17:{jnana[2]}->18:{jnanaArrive[2]}')
                    
                    
                else:
                        print('\nEnter a valid number')
                        continue
            #18時
        elif current==18:
                jhachi=[17,36]
                print(f' 18:0{jhachi[0]}, 18:{jhachi[1]}')
                choice=int(input('\nご利用する列車を１～２の中からお選びください。'))
                if choice>=1 and choice<=2:
                    jhachiArrive=[31,52]
                    if choice==1:
                        print(f'18:{jhachi[0]}->18:{jhachiArrive[0]}')
                    elif choice==2:
                        print(f'18:{jhachi[1]}->18:{jhachiArrive[1]}')
                    
                    
                    
                else:
                        print('\nEnter a valid number')
                        continue
            #19時
        elif current==19:
                jkyuu=[6,31,44]
                print(f' 19:0{jkyuu[0]}, 19:{jkyuu[1]}, 19:{jkyuu[2]}')
                choice=int(input('\nご利用する列車を１～３の中からお選びください。'))
                if choice>=1 and choice<=3:
                    jkyuuArrive=[21,44,58]
                    if choice==1:
                        print(f'19:0{jkyuu[0]}->19:{jkyuuArrive[0]}')
                    elif choice==2:
                        print(f'19:{jkyuu[1]}->19:{jkyuuArrive[1]}')
                    elif choice==3:
                        print(f'19:{jkyuu[2]}->19:{jkyuuArrive[2]}')
                    
                    
                else:
                        print('\nEnter a valid number')
                        continue
            #20時
        elif current==20:
                nij=[1,11,39]
                print(f' 20:0{nij[0]}, 20:{nij[1]}, 20:{nij[2]}')
                choice=int(input('\nご利用する列車を１～３の中からお選びください。'))
                if choice>=1 and choice<=3:
                    nijArrive=[15,28,53]
                    if choice==1:
                        print(f'20:0{nij[0]}->20:{nijArrive[0]}')
                    elif choice==2:
                        print(f'20:{nij[1]}->20:{nijArrive[1]}')
                    elif choice==3:
                        print(f'20:{nij[2]}->20:{nijArrive[2]}')
                    
                    
                else:
                        print('\nEnter a valid number')
                        continue
            #21時  
        elif current==21:
                niichi=[5,16,42,55]
                print(f' 21:{niichi[0]}, 21:{niichi[1]}, 21:{niichi[2]}, 21:{niichi[3]}')
                choice=int(input('\nご利用する列車を１～４の中からお選びください。'))
                if choice>=1 and choice<=4:
                    niichiArrive=[19,31,56,13]
                    if choice==1:
                        print(f'21:0{niichi[0]}->21:{niichiArrive[0]}')
                    elif choice==2:
                        print(f'21:{niichi[1]}->21:{niichiArrive[1]}')
                    elif choice==3:
                        print(f'21:{niichi[2]}->21:{niichiArrive[2]}')
                    elif choice==4:
                        print(f'21:{niichi[3]}->22:0{niichiArrive[3]}')
                else:
                        print('\nEnter a valid number')
                        continue
            #22時
        elif current==22:
                nini=[16,33,52]
                print(f' 22:{nini[0]}, 22:{nini[1]}, 22:{nini[2]}')
                choice=int(input('\nご利用する列車を１～３の中からお選びください。'))
                if choice>=1 and choice<=3:
                    niniArrive=[31,47,6]
                    if choice==1:
                        print(f'22:{nini[0]}->22:{niniArrive[0]}')
                    elif choice==2:
                        print(f'22:{nini[1]}->22:{niniArrive[1]}')
                    elif choice==3:
                        print(f'22:{nini[2]}->23:0{niniArrive[2]}')
                    
                    
                else:
                        print('\nEnter a valid number')
                        continue
            #23時
        elif current==23:
                nisan=[17,45]
                print(f' 23:{nisan[0]}, 23:{nisan[1]}')
                choice=int(input('\nご利用する列車を１～２の中からお選びください。'))
                if choice>=1 and choice<=2:
                    nisanArrive=[31,59]
                    if choice==1:
                        print(f'23:{nisan[0]}->23:{nisanArrive[0]}')
                    elif choice==2:
                        print(f'23:{nisan[1]}->23:{nisanArrive[1]}')
                    
                    
                    
                else:
                        print('\nEnter a valid number')
                        continue
            #24時
        elif current==24:
                 print('00:06->00:20')
        else:
             print('\nEnter a valid number 5~24')
            
    else:
        print('\nEnter a valid number 5~24')
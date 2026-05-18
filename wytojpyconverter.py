#converter for Japanese years and Western years

while True:
    c=int(input('Enter 1 to convert western year to Japanese year\nEnter 2 to convert Japanese year to western year\nEnter anything else to end the program: '))
    #Convert to Japanese year
    if c==1:
        wy=int(input('Enter a western year: '))
        if wy>=1926 and wy<=1988:
                s=wy-1925
                print(f"昭和{s}年")
        elif wy==1989:
               print(f"昭和64年/平成1年")
        elif wy>1989 and wy<=2018:
                h=wy-1988
                print(f"平成{h}年")
        elif wy==2019:
               print(f"平成31年/令和1年")        
        elif wy>2019 and wy<=2026:
                r=wy-2018
                print(f"令和{r}年")
        elif wy>2026:
              print('2026年より後はまだ変換できません。')
        else:
                print('Error')
    #Convert to Western year
    elif c==2:
        jy=int(input('Enter 1 for Showa,2 for Heisei,3 for Reiwa: '))
        if jy==1:
                jys=int(input('Enter which year of Showa era: '))
                if jys>=1 and jys<=64:
                    jys=jys+1925
                    print(jys)
                else:
                    print('昭和時代は64年までです。')
        elif jy==2:
                jyh=int(input('Enter which year of Heisei era: '))
                if jyh>=1 and jyh<=31:
                    jyh=jyh+1988
                    print(jyh)
                else:
                    print('平成時代は31年までです。')
        elif jy==3:
                jyr=int(input('Enter which year of Reiwa era: '))
                if jyr>=1 and jyr<=8:
                    jyr=jyr+2018
                    print(jyr)
                else:
                    print('2026年より後はまだ変換できません。')
        else:
                print('Error')
    else:
        break

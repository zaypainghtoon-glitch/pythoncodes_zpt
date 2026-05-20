money=int(input('Enter less than 1000 yen'))
gohyaku=0
hyaku=0
gojyuu=0
jyuu=0
go=0
ichi=0
if money<1000 and money>=0:
    while money>=500 and money<1000:
        money=money-500
        gohyaku+=1
    while money>=100 and money<500:
        money=money-100
        hyaku+=1
           
    while money>=50 and money<100:
        money=money-50
        gojyuu+=1
    while money>=10 and money<50:
        money=money-10
        jyuu+=1
    while money>=5 and money<10:
        money=money-5
        go+=1
    while money>=1 and money<5:
        money=money-1
        ichi+=1
elif money==0:
    exit()
print(f"500円:{gohyaku}枚\n100円:{hyaku}枚\n50円:{gojyuu}枚\n10円{jyuu}枚\n5円:{go}枚\n1円:{ichi}枚\n")
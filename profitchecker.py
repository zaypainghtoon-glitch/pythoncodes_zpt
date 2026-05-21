#profit checker

products={'Egg':200,'Milk':300,'Bread':150}
youbi=['月','火','水','木','金','土','日']

weekProfit=0


addProfit=0
def profitcheckerdaybyday():
    soldEgg=int(input('今日売れた卵の数を入力してください: '))
    profitFromEgg=products['Egg']*soldEgg
    print(f"卵からの利益：{profitFromEgg}円\n")

    soldMilk=int(input('今日売れた牛乳の数を入力してください: '))
    profitFromMilk=products['Milk']*soldMilk
    print(f"牛乳からの利益：{profitFromMilk}円\n")

    soldBread=int(input('今日売れたパンの数を入力してください: '))
    profitFromBread=products['Bread']*soldBread
    print(f"パンからの利益：{profitFromBread}円\n")

    profit=profitFromEgg+profitFromBread+profitFromMilk
    print(f"今日の利益：　{profit}円\n")
    return profit
    


for day in youbi:
        print(f"今日は{day}曜日です。")
        dailyProfit=profitcheckerdaybyday()
        weekProfit+=dailyProfit
          
print(f"今週の利益:{weekProfit}円")

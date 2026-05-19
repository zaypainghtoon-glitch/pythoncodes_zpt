#Turn based RPG battle for 2v3 battle
#19/5/2026
import random

line=('-'*75)

while True:

    player_name=str(input('Enter your name: '))

    player_stats={'name':player_name,'attack':50,'hp':500,'speed':32}
    Alice_stats={'name':'Alice','attack':50,'hp':400,'speed':22}

    goblin1_stats={'name':'Goblin 1','attack':50,'hp':300,'speed':25}
    goblin2_stats={'name':'Goblin 2','attack':50,'hp':300,'speed':20}
    goblin3_stats={'name':'Goblin 3','attack':50,'hp':300,'speed':12}

    turnOrder=[
        player_stats,
        Alice_stats,
        goblin1_stats,
        goblin2_stats,
        goblin3_stats
    ]

    turnOrder.sort(key=lambda character: character['speed'],reverse=True)

    print(line)
    print('Turn Order')
    print(line)
    while (
    (player_stats['hp'] > 0 or Alice_stats['hp'] > 0)
    and
    ( goblin1_stats['hp'] > 0 or goblin2_stats['hp'] > 0 or goblin3_stats['hp'] > 0)):

        for character in turnOrder:
                turnOrder=[
                    player_stats,
                    Alice_stats,
                    goblin1_stats,
                    goblin2_stats,
                    goblin3_stats
                ]

                turnOrder.sort(key=lambda character: character['speed'],reverse=True)
                #removes the defeated character
                turnOrder = [
                    character
                    for character in turnOrder
                    if character['hp'] > 0
                ]

                
                #player's attack
                print(f"{character['name']}'s turn")
                
                if character==player_stats:
                    target_choice=int(input('Choose 1 to 3 to who you want to attack: '))

                    if target_choice==1:
                        target_enemy=goblin1_stats
                        damage=player_stats['attack']*2
                        goblin1_stats['hp']-=damage
                        print(f"{player_stats['name']} used Double Sword attack.")
                        print(line)
                        print(f"{player_stats['name']} attacked {goblin1_stats['name']} for {damage} damage.\n")
                        
                        print(f"Goblin 1's HP: {goblin1_stats['hp']}\n")
                        print(line)
                        print('Current HP of all characters:')
                        for character in turnOrder:
                            print(f"{character['name']}'s HP:{character['hp']} ")
                        print(line)
                        print(line) 
                        
                        continue
                        
                        
                        

                    elif target_choice==2:
                        target_enemy=goblin2_stats
                        damage=player_stats['attack']*2
                        goblin2_stats['hp']-=damage
                        print(f"{player_stats['name']} used Double Sword attack.")
                        print(line)
                        print(f"{player_stats['name']} attacked {goblin2_stats['name']} for {damage} damage.\n")
                        print(f"Goblin 2's HP: {goblin2_stats['hp']}\n")
                        print(line)
                        print('Current HP of all characters:')
                        for character in turnOrder:
                            print(f"{character['name']}'s HP:{character['hp']} ")
                        print(line)
                        print(line)    
                        
                        continue

                    elif target_choice==3:
                        target_enemy=goblin3_stats
                        damage=player_stats['attack']*2
                        goblin3_stats['hp']-=damage
                        print(f"{player_stats['name']} used Double Sword attack!!")
                        print(line)
                        print(f"{player_stats['name']} attacked {goblin1_stats['name']} for {damage} damage.\n")
                        print(f"Goblin 3's HP: {goblin3_stats['hp']}\n")
                        print(line)
                        print('Current HP of all characters:')
                        for character in turnOrder:
                            print(f"{character['name']}'s HP:{character['hp']} ")
                        print(line)
                        print(line)    
                        continue
                        
                    else:
                        ('You missed the attack.\n')
                        print(line)
                        print(line)
                        continue
                #Alice's attack
                elif character==Alice_stats:
                    target_choice=int(input(f"Press 1 to use Alice's AoE attack: "))
                    if target_choice==1:
                        damage=Alice_stats['attack']/1.5
                        goblin1_stats['hp']-=damage
                        goblin2_stats['hp']-=damage
                        goblin3_stats['hp']-=damage
                        print('Alice used Magic Bomb!!')
                        print(line)
                        print(f"Alice attacked all enemies for {damage} damage.")
                        print(line)
                        print('Current HP of all characters:')
                        for character in turnOrder:
                            print(f"{character['name']}'s HP:{character['hp']} ")
                        print(line)
                        print(line)    
                        continue
                    else:
                        print('Alice missed her attack.')
                        print(line)
                #goblin 1 AI attack
                elif character==goblin1_stats:
                    target_choice=random.randint(1,2)
                    if target_choice==1:
                        print('Goblin 1 attacked player with Goblin Spear!!')
                        print(line)
                        damage=goblin1_stats['attack']
                        player_stats['hp']-=damage
                        print(f"Goblin 1 attacked player for {damage} damage.")
                        print(line)
                        print('Current HP of all characters:')
                        for character in turnOrder:
                            print(f"{character['name']}'s HP:{character['hp']} ")
                        print(line)
                        print(line)    
                        continue
                    else:
                        print('Goblin 1 attacked Alice with Goblin Spear!!')
                        print(line)
                        damage=goblin1_stats['attack']
                        Alice_stats['hp']-=damage
                        print(f"Goblin 1 attacked Alice for {damage} damage.")
                        print(line)
                        print('Current HP of all characters:')
                        for character in turnOrder:
                            print(f"{character['name']}'s HP:{character['hp']} ")
                        print(line)
                        print(line)   
                        continue
                #goblin 2 AI attack
                elif character==goblin2_stats:
                    target_choice=random.randint(1,2)
                    if target_choice==1:
                        print('Goblin 2 attacked player with Goblin Spear!!')
                        print(line)
                        damage=goblin2_stats['attack']
                        player_stats['hp']-=damage
                        print(f"Goblin 2 attacked player for {damage} damage.")
                        print(line)
                        print('Current HP of all characters:')
                        for character in turnOrder:
                            print(f"{character['name']}'s HP:{character['hp']} ")
                        print(line)
                        print(line)    
                        continue
                    else:
                        print('Goblin 2 attacked Alice with Goblin Spear!!')
                        print(line)
                        damage=goblin1_stats['attack']
                        Alice_stats['hp']-=damage
                        print(f"Goblin 2 attacked Alice for {damage} damage.")
                        print(line)
                        print('Current HP of all characters:')
                        for character in turnOrder:
                            print(f"{character['name']}'s HP:{character['hp']} ")
                        print(line)
                        print(line)    
                        continue
                #goblin 3 AI attack
                elif character==goblin3_stats:
                    target_choice=random.randint(1,2)
                    if target_choice==1:
                        print('Goblin 3 attacked player with Goblin Spear!!')
                        print(line)
                        damage=goblin3_stats['attack']
                        player_stats['hp']-=damage
                        print(f"Goblin 3 attacked player for {damage} damage.")
                        print(line)
                        print('Current HP of all characters:')
                        for character in turnOrder:
                            print(f"{character['name']}'s HP:{character['hp']} ")
                        print(line)
                        print(line)    
                        continue
                    else:
                        print('Goblin 3 attacked Alice with Goblin Spear!!')
                        print(line)
                        damage=goblin1_stats['attack']
                        Alice_stats['hp']-=damage
                        print(f"Goblin 3 attacked Alice for {damage} damage.")
                        print(line)
                        print('Current HP of all characters:')
                        for character in turnOrder:
                            print(f"{character['name']}'s HP:{character['hp']} ")
                        print(line)
                        print(line)    
                        continue    
    if goblin1_stats['hp']<=0 and goblin2_stats['hp']<=0 and goblin3_stats['hp']<=0:
        print('\nYou have defeated the enemies.')
        print(line)
        break
    else:
        print('\nYou and your compainions are defeated.')         
        print(line)
        break   
    
                
            
            



    
    

#TerminalRPG

import random
import msvcrt

#start menu
print('Press any key to start')
msvcrt.getch()

party_member=[]
inventory=[]
gold=0
while True:

    #line for clearer visibility
    line=('-'*100)
    #Greeting the player
    print('\nHello Adventurer!')
    name=str(input('May I ask you for your name:'))
    print(line)
    print(f"\nWelcome to the Adventurer's guild {name}.You can complete a various missions to earn money and buy items.\nYou can also recruit party members and your ultimate goal is to defeat the MARAS who is one of the loyal servant of Demon King.\n")

    #Race selection
    print(line)
    race_choose_or_random=int(input('Enter 1 to choose the race or Enter any number to randomize your race.'))

    #Choosing the race
    if race_choose_or_random==1:
        race=['Elf','Orc','Dwarf','Human']
        while True:
            print(race)
            chosenrace=int(input('Enter 1 to 4 to choose your race from the list.'))
            print(line)
            
            if chosenrace>=1 and chosenrace<=4:
                print(f"You are a/an {race[chosenrace-1]}.")
                print(line)
                race_confirm=int(input('Are you sure about your choice(1=Yes,2=No)\n'))
                print(line)
                if race_confirm==1:
                    print(f"You are now a/an {race[chosenrace-1]}.\n")
                    print(line)
                    break
                elif race_confirm==2:
                    print('\nEnter 1 to 4 to choose your race from the list.')
                    print(line)
                else:
                    print('Invalid confirmation.')
                    print(line)

                
            else:
                print('Enter a valid number which is 1 to 4')
                print(line)

    #Randomizing the race
    else:
        race=['Elf','Orc','Dwarf','Human']
        randomrace=random.choice(race)
        print(f"You are a/an {randomrace}.")
        print(line)

    #choosing role
    role=['Warrior','Ranger','Mage','Healer']
    print(role)
    choosing_role=int(input('\nEnter 1 to 4 to choose your role from the list.'))
    print(line)
    
    if choosing_role>=1 and choosing_role<=4:
        print(f"You are a {role[choosing_role-1]}.")
        print(line)
        
        if choosing_role==1:
            print('This will be your stats.\n')
            player_stats={'Attack_Power':100,'Magic_Power':10,'Health_Point':500,'Speed':50,'Level':1}
            print(player_stats)
            print(line)
        elif choosing_role==2:
            print('This will be your stats.\n')
            player_stats={'Attack_Power':150,'Magic_Power':10,'Health_Point':450,'Speed':70,'Level':1}
            print(player_stats)
            print(line)
        elif choosing_role==3:
            print('This will be your stats.\n')
            player_stats={'Attack_Power':10,'Magic_Power':150,'Health_Point':450,'Speed':30,'Level':1}
            print(player_stats)
            print(line)
        elif choosing_role==4:
            print('This will be your stats.\n')
            player_stats={'Attack_Power':10,'Magic_Power':100,'Health_Point':500,'Speed':30,'Level':1}
            print(player_stats)
            print(line)
        else:
            print('Invalid choice\n')
            print(line)
    else:
        print('Invalid choice.')
        print(line)  

    
    

    #first battle
    print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    print(line)
    slime_stats={'Attack_Power':50,'Magic_Power':10,'Health_Point':300,'Speed':30,'Level':1}

    while player_stats['Health_Point']>0 and slime_stats['Health_Point']>0:
        if choosing_role==1 or choosing_role==2:
            #player turn for Warrior & Ranger
            print('\nYour turn')

            player_turn_choice=int(input('\nPress 1 to attack 2 to open the item menu: '))
            if player_turn_choice==1:
                player_attack = player_stats['Attack_Power']
                #crit line for player
                crit_chance = 0.2
                crit_multiplier = 2

                damage = player_attack

                if random.random() < crit_chance:
                    damage *= crit_multiplier
                    print('\nCritical Hit!!!')

                slime_stats['Health_Point'] -= damage


                if slime_stats['Health_Point']<0:
                    slime_stats['Health_Point']=0

                print(f"\nYou attacked the slime for {damage} damage.")
                print(f"\nSlime HP is {slime_stats['Health_Point']}")
                gold+=100
                print(f"\nYou gained {gold} gold.")
                print(line)

            elif player_turn_choice==2:
                print(inventory)

        else:
            #player turn for Mage & Healer
            print('\nYour turn')

            player_turn_choice=int(input('\nPress 1 to attack 2 to open the item menu: '))

            if player_turn_choice==1:

                player_attack = player_stats['Magic_Power']
                #crit line for player
                crit_chance = 0.2
                crit_multiplier = 2

                damage = player_attack

                if random.random() < crit_chance:
                    damage *= crit_multiplier
                    print('\nCritical Hit!!!')

                slime_stats['Health_Point'] -= damage


                if slime_stats['Health_Point']<0:
                    slime_stats['Health_Point']=0

                print(f"\nYou attacked the slime for {damage} damage.")
                print(f"\nSlime HP is {slime_stats['Health_Point']}")
                print(line)
            elif player_turn_choice==2:
                print(inventory)

        #check if slime died
        if slime_stats['Health_Point']<=0:
            print('\nYou defeated the slime!!!')
            print(line)
            #Leveling up the player
            player_stats['Level']+=1
            print(f"\nYou are upgraded to {player_stats['Level']}\n.")
            player_stats['Attack_Power']+=20
            player_stats['Health_Point']+=20
            player_stats['Magic_Power']+=20
            print(player_stats)
            print(line)

            print('bbbbbbbbbbbbbbbbbbbbbbbbbb')
            inventory.append('Health Potion')
            
            break
        

        #slime turn
        print('\nEnemy turn')

        slime_attack=slime_stats['Attack_Power']
        #crit line for slime
        crit_chance=0.2
        crit_multiplier=2

        damage=slime_attack

        if random.random()<crit_chance:
            damage*=crit_multiplier
            print('\nCritical Hit!!!')

        player_stats['Health_Point']-=damage

        
        #not showing negative HP
        if player_stats['Health_Point']<0:
            player_stats['Health_Point']=0

        print(f"\nSlime attacked the player for {damage} damage.")
        print(f"\nPlayer HP is {player_stats['Health_Point']}")
        print(line)
        #check if player died
        if player_stats['Health_Point']<=0:
            print('Slime defeated the player')
            print(line)
            break

    
    

    print('ccccccccccccccccccccccccccccccccccccccccccc')

    
    
    #recruiting
    companions_stats = {
    'Alice': {'Attack_Power':100,'Magic_Power':10,'Health_Point':500,'Speed':50,'Level':1},
    'Bane': {'Attack_Power':150,'Magic_Power':10,'Health_Point':450,'Speed':70,'Level':1},
    'Nana': {'Attack_Power':10,'Magic_Power':150,'Health_Point':450,'Speed':30,'Level':1},
    'Estes': {'Attack_Power':10,'Magic_Power':100,'Health_Point':500,'Speed':30,'Level':1}
    }
    recruitable=['Alice','Bane','Nana','Estes']
    print(recruitable)
    print(line)
    recruit_choice=int(input('\nEnter 1 to 4 to choose '))
    print(line)
    
    if recruit_choice>=1 and recruit_choice<=4:
        chosen_companion = recruitable[recruit_choice - 1]

        print(f"\nYou have chosen {chosen_companion}.")
        print(companions_stats[chosen_companion])
        gold-=50
        print("You paid {gold} gold.")
        party_member.append(companions_stats)

    #to the dungeon with companion

    print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    print(line)

    #dungeon stage 1

    print('\nA group of goblins appered!!')

    goblin_group={'gob1':{'Attack_Power':70,'Magic_Power':10,'Health_Point':350,'Speed':30,'Level':2},
                  'gob2':{'Attack_Power':70,'Magic_Power':10,'Health_Point':350,'Speed':30,'Level':2},
                  'gob3':{'Attack_Power':70,'Magic_Power':10,'Health_Point':350,'Speed':30,'Level':2}
    }
    

    #------------------Pasued code because I feel stucked-----------------------
    #14/5/2026



            





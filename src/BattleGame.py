#Author: Elvis Cao
#Description: The program takes the user through a dungeon filled with monsters.
#There are various enemies to defeat throughout various stages.

import random

def KillPlayer():
    print("Game Over. The hero has fallen.")
def StageClear():
    print("Congratulations! You won!")
def TurnTimer():
    print("You took too long. The hero has fallen.")
def Stage1():
    Player_HP = 250
    Goblin_HP = 250
    print("You own a broadsword")
    print("Broadsword Power: 23~48")
    print("Broadsword Crit Dmg: 78~122")
    print("Broadsword Crit Rate: 50%")
    print("Healing Oath: HP +50~150")
    print("Goblin Attack: 25~100")
    print("Player_HP:", Player_HP, "HP")
    print("Goblin_HP:", Goblin_HP, "HP")
    print("A goblin appears before you. What action will you take?")
    for turn in range (1, 11):
        user_action = int(input("Attack: 0 or Healing Oath: 1\n"))
        if user_action == 1:
            print("You heal")
            Player_HP += random.randint(50, 150)
            if Player_HP > 250:
                Player_HP = 250
            print("Player_HP:", Player_HP, "HP")
            print("Goblin_HP:", Goblin_HP, "HP")
            print("The goblin strikes you")
            Player_HP -= random.randint(25, 100)
            print("Player_HP:", Player_HP, "HP")
            if Player_HP <= 0:
                KillPlayer()
                victory = 'loss'
                break
        else:
            print("You attack the goblin")
            crit = random.randint(3,4)
            if crit == 3:
                Goblin_HP -= random.randint(23, 48)
                print("Goblin_HP:", Goblin_HP, "HP")
            else:
                print("You scored a critical hit on the goblin!")
                Goblin_HP -= random.randint(78, 122)
                print("Goblin_HP:", Goblin_HP, "HP")
            if Goblin_HP <= 0:
                StageClear()
                gold = random.randint(50, 500)
                print("You received", gold, "gold for winning.")
                victory = 'win'
                break
            print("The goblin strikes you")
            Player_HP -= random.randint(25, 100)
            print("Player_HP:", Player_HP, "HP")
            if Player_HP <= 0:
                KillPlayer()
                victory = 'loss'
                break
    else:
        if turn == 10:
            TurnTimer()
            print("You took a total of", turn, "turns.")
            victory = 'loss'
            return victory
    print("You took a total of", turn, "turns.")
    return victory
def Stage2():
    Player_HP = 500
    Troll_HP = 600
    print("Stage 2")
    print("You now own a Claymore")
    print("Claymore Power: 69~109")
    print("Claymore Crit Dmg: 144~225")
    print("Claymore Crit Rate: 66.667%")
    print("Claymore Accuracy: 75%")
    print("Healing Oath: HP +15~275")
    print("Troll Attack: 10~200")
    print("Player HP:", Player_HP, "HP")
    print("Troll_HP:", Troll_HP, "HP")
    print("A troll appears before you. What action will you take?")
    for turn in range (1, 13):
        Burst_Dmg = 0
        if turn == 5:
            print("You have awakened. Damage dealt increased!")
        if turn >= 5:
            Burst_Dmg = random.randint(50, 100)
        user_action = int(input("Attack: 0 or Healing Oath: 1\n"))
        if user_action == 1:
            print("You heal")
            Player_HP += random.randint(15, 275)
            if Player_HP > 500:
                Player_HP = 500
            print("Player_HP:", Player_HP, "HP")
            print("Troll_HP:", Troll_HP, "HP")
            print("The troll strikes you")
            Player_HP -= random.randint(10, 200)
            print("Player_HP:", Player_HP, "HP")
            if Player_HP <= 0:
                KillPlayer()
                victory = 'loss'
                break
        else:
            accuracy = random.randint(1,4)
            if accuracy == 4:
                print("You missed and did 0 damage")
                print("Troll_HP:", Troll_HP, "HP")
                print("The troll strikes you")
                Player_HP -= random.randint(10, 200)
                print("Player_HP:", Player_HP, "HP")
                if Player_HP <= 0:
                    KillPlayer()
                    victory = 'loss'
                    break
            else:
                print("You attacked the troll")
                crit = random.randint(3,5)
                if crit == 3:
                    Troll_HP -= random.randint(69, 109)
                    Troll_HP -= Burst_Dmg
                    print("Troll_HP:", Troll_HP, "HP")
                else:
                    print("You scored a critical hit on the troll!")
                    Troll_HP -= random.randint(144, 225)
                    Troll_HP -= Burst_Dmg
                    print("Troll_HP:", Troll_HP, "HP")
                if Troll_HP <= 0:
                    StageClear()
                    gold = random.randint(50, 1000)
                    print("You received", gold, "gold for winning.")
                    victory = 'win'
                    break
                print("The troll strikes you")
                Player_HP -= random.randint(10, 200)
                print("Player_HP:", Player_HP, "HP")
                if Player_HP <= 0:
                    KillPlayer()
                    victory = 'loss'
                    break
    else:
        if turn == 12:
            TurnTimer()
            print("You took a total of", turn, "turns.")
            victory = 'loss'
            return victory
    print("You took a total of", turn, "turns.")
    return victory
def Stage3():
    Player_HP = 2300
    Dragon_HP = 4000
    print("You now own a polearm")
    print("Polearm Power: 188~304")
    print("Polearm Crit Dmg: 425~801")
    print("Polearm Crit Rate: 50%")
    print("Healing Oath: HP +125~500")
    print("Dragon Attack: 150~400")
    print("Dragon Crit Dmg: 450~750")
    print("Dragon Crit Rate: 25%")
    print("Player HP:", Player_HP, "HP")
    print("Dragon_HP:", Dragon_HP, "HP")
    print("A gigantic flame dragon appears before you. What action will you take?")
    for turn in range(1, 21):
        bonus_dmg = 0
        if turn == 2:
            print("The angels have appeared to bless you.")
        if turn >= 2 and turn % 2 == 0:
            print("The angels heal you")
            Player_HP += random.randint(100,200)
            print("Player HP:", Player_HP, "HP")
        if turn == 8:
            print("The dragon is filled with rage")
        if turn >= 8:
            bonus_dmg = random.randint(50, 100)
        user_action = int(input("Attack: 0 or Healing Oath: 1\n"))
        if user_action == 1:
            print("You heal")
            Player_HP += random.randint(125, 500)
            if Player_HP > 1500:
                Player_HP = 1500
            print("Player_HP:", Player_HP, "HP")
            print("Dragon_HP:", Dragon_HP, "HP")
            print("The dragon scorches you")
            d_crit = random.randint(5, 8)
            if d_crit == 8:
                print("The dragon scorches intense flames that burn your bones")
                Player_HP -= random.randint(450, 750)
                Player_HP -= bonus_dmg
            else:
                Player_HP -= random.randint(150, 400)
                Player_HP -= bonus_dmg
            print("Player_HP:", Player_HP, "HP")
            if Player_HP <= 0:
                KillPlayer()
                victory = 'loss'
                break
        else:
            print("You pierce the dragon")
            crit = random.randint(3,4)
            if crit == 3:
                Dragon_HP -= random.randint(188, 304)
                print("Dragon_HP:", Dragon_HP, "HP")
            else:
                print("You scored a critical hit on the dragon!")
                Dragon_HP -= random.randint(425, 801)
                print("Dragon_HP:", Dragon_HP, "HP")
            if Dragon_HP <= 0:
                StageClear()
                gold = random.randint(500, 5000)
                print("You received", gold, "gold for winning.")
                victory = 'win'
                break
            print("The dragon scorches you")
            d_crit = random.randint(5, 8)
            if d_crit == 8:
                print("The dragon scorches intense flames that burn your bones")
                Player_HP -= random.randint(450, 750)
                Player_HP -= bonus_dmg
            else:
                Player_HP -= random.randint(150, 400)
                Player_HP -= bonus_dmg
            print("Player_HP:", Player_HP, "HP")
            if Player_HP <= 0:
                KillPlayer()
                victory = 'loss'
                break
    else:
        if turn == 20:
            TurnTimer()
            print("You took a total of", turn, "turns.")
            victory = 'loss'
            return victory
    print("You took a total of", turn, "turns.")
    return victory
            
            
if __name__ == "__main__":
    print("Welcome to Tower of Death.")
    print("Stage 1")
    result = Stage1()
    if result == 'win':
        result_2 = Stage2()
        if result_2 == 'win':
            print("Stage 3")

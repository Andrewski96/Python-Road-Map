import random

def choiceMake(): #Function used to gather players direction input
    decide = input("Enter what direction you wish to go (L or R) or Q to give up: ")
    decideUp = decide.upper() #This is to ensure all input a user enters is in uppercase to make casing easier.
    return decideUp
def attackMovement(atkStat): #Function used to compound the ATK stat with itself
    atkStat += random.randint(1,3)
    return atkStat
def hpMovement(hpStat): #Function used to compound the HP stat with itself
    hpStat += random.randint(1,5)
    return hpStat


leftMove = rightMove = HP = ATK = bossHP = bossATK = 0
bossHP += random.randint(10,35)
bossATK += random.randint(2,8)
print("You see an entrance to an impossible maze in front of you where you can take 8 lefts in a row if you wish! \nYou hear in the wind, LEFT grants you health, while RIGHT grants you POOOWWWEER!!")

#The while loop will always be true unless a break occurs, this is easier than comparing both leftMove AND rightMove. It is half the work, as just one breaching is needed to break the loop.
while True:
    print(f'Stats: {HP} HP || {ATK} ATK')
    tempL = leftMove #Added a temp here to compare it later on and determine to use hpMovement()
    tempR = rightMove #Added a temp here to compare it later on and determine to use attackMovement()
    value = choiceMake()
    if value == 'L': #Case would be easier to use here, but since it is only comparing 3 values, I decided to just use if, elif and else.
        leftMove += 1
        if leftMove == 5:
            break
    elif value == 'R':
        rightMove += 1
        if rightMove == 5:
            break
    elif value == 'Q':
        print("Quitters aren't winners. GG")
        break
    else:
        print("Please enter a correct route of L) eft or R) ight")
    if leftMove > tempL: #Used to compare what the value was before player played their turn. If leftMove was the variable affected, this would be true, meaning the player chose left.
        HP = hpMovement(HP)
    elif rightMove > tempR: #Used to compare what the value was before player played their turn. If rightMove was the variable affected, this would be true, meaning the player chose right.
        ATK = attackMovement(ATK)
print("\n")

#Fight sequence
roundNum =1
while bossHP >= 0 or HP >= 0:
    if value == 'Q': #Added this line of code to end the while loop if the player quit earlier, so it doesn;t do the fight sequence.
        break
    print(f'Fight! Round {roundNum}')
    roundNum+= 1
    print(f'HP: {HP} ATK: {ATK} || Boss HP: {bossHP} Boss ATK: {bossATK}')
    print(f'You attack the boss and deal {ATK} damage.')
    bossHP -= ATK
    if bossHP <= 0: #If Boss' HP reaches 0 or less, this will make their HP = 0 and not a negative, then print the statement and end the loop.
        bossHP = 0
        print('You defeated the mighty boss!! Hurrah!')
        break
    print(f'Boss has {bossHP} health left.\n')
    print(f'Boss man attacks you and deals {bossATK} damage')
    HP -= bossATK
    if HP <= 0: #If player HP reaches 0 or less, this will make their HP = 0 and not a negative, then print the statement and end the loop.
        HP = 0
        print('YOU DIED!!!!!! GAME OVER.')
        break
    print(f'You have {HP} health left.\n')
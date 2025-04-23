import random

print("I\'m thinknig of a number between 1 and 10. Can you guess it?")
guess = int(input('Your guess: '))
answer = random.randint(1,10)
count = 1
while guess != answer:
    if guess > answer:
        print('Too high! Try again.')
        count +=1
    elif guess < answer:
        print('Too low! Try again.')
        count +=1
    guess = int(input('Your guess: '))
print(f'Correct! You guess the number in {count} attempts.')
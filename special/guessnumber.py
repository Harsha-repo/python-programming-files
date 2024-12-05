import random
secret_number=random.randint(1,10)
print('im thinking of number between one and twenty ')
for guesstaken in range(1,7) :
    guess= int(input())

    if guess<secret_number:
        print('your guess is too low ')

    elif guess >secret_number :
        print('your guess is too high')
    else :
        print('goodjob! you guessed my number in '+str(guesstaken)+'guesses')
        
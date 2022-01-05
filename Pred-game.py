from random import randint

#v0.0.0002 # исправлен баг с wrong conditions

wins = 0
looses = 0
#AI_num = randint(1, 10)
while True:
    AI_num = randint(1, 1000)
    your_num = input('Please enter your number from 1 to 1000: ')
    if your_num == 'exit':
        print('GoodBye !')
        break
    elif your_num == 'stat':
        print(f'wins = {wins}, looses = {looses}')
    elif int(your_num) < 1 or int(your_num) > 1000:
        print('Wrong conditions, please try again') 
        continue
    elif int(your_num) == AI_num:
        print('You win !!!')
        print(f'Here yout stats: wins = {wins}, looses = {looses}')
        wins += 1
        break
    elif int(your_num) != AI_num:
        print('You loos :(')
        looses += 1
        continue
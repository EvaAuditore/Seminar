from random import randint

total_candies = 2021
take_candies = 0
player_1_candies = 0
player_2_candies = 0

def start_game():
    print()
    print('Привет, сейчас вам предстоит сыграть в интересную игру=) Для начала\n')
    global player_1
    global player_2
    player_1 = input('Введите имя, пожалуйста: \n')
    player_2 = input('Введите имя, пожалуйста: \n')

def turn():
    '''
    Определение очередности
    '''
    turn_players = randint(0, 2)
    if turn_players == 0:
        print(f'Первым ходит игрок {player_1}')
        player_1_turn()   
    else:
        print(f'Первым ходит игрок {player_2}')
        player_2_turn()
        
def player_1_turn():
    global total_candies
    global take_candies
    global player_1_candies
    print(f'На столе {total_candies} конфет')
    take_candies = int(input(f'{player_1}, cколько возьмете конфет?\n'))
    while take_candies < 0 or take_candies > 28 or take_candies > total_candies:
        take_candies = int(input(f'{player_1},Возьмите корректное число конфет: \n'))
    total_candies -= take_candies
    player_1_candies += take_candies
    if total_candies > 0:
        player_2_turn()
    else:
        print(f'{player_1}, Вы выиграли! Поздравляем!')
        


def player_2_turn():
    global total_candies
    global take_candies
    global player_2_candies
    print(f'На столе {total_candies} конфет')
    take_candies = int(input(f'{player_2},cколько возьмете конфет?\n'))
    while take_candies < 0 or take_candies > 28 or take_candies > total_candies:
        take_candies = int(input(f'{player_2},возьмите корректное число конфет: \n'))
    total_candies -= take_candies
    player_2_candies += take_candies
    if total_candies > 0:
        player_1_turn()
    else:
        print(f'{player_2},Вы выиграли! Поздравляем!')
    

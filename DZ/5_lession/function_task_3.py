from random import randint


field = list(range(1, 10))

winning_options = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]

def start_game():
    print()
    print('Привет, сейчас вам предстоит сыграть в крестики-нолики=) Для начала\n')
    global player_1
    global player_2
    player_1 = input('Введите имя, пожалуйста: \n')
    player_2 = input('Введите имя, пожалуйста: \n')


def create_field():
    print('------------')
    for i in range(3):
        print('|', field[0+i*3], '|', field[1+i*3], '|', field[2+i*3], '|')
        print('------------')


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
    marker_1 = ('x')
    
    while True:
        value = int(input(f'{player_1}, куда хотите поставить {marker_1}: \n'))
        field[value-1] = marker_1
        break
    for each in winning_options:
        if(field[each[0]-1]) == (field[each[1]-1]) == (field[each[2]-1]):  #не очень понимаю, как это работает пока=)
            print('Победа!')
            create_field()
            return field[each[1]-1]
            
    else:
        create_field()
        player_2_turn()


def player_2_turn():
    marker_2 = ('o')
    while True:
        value = int(input(f'{player_2}, куда хотите поставить {marker_2}: \n'))
        field[value-1] = marker_2
        break
    for each in winning_options:
        if(field[each[0]-1]) == (field[each[1]-1]) == (field[each[2]-1]):
            print('Победа!')
            create_field()
            return field[each[1]-1]
            
    else:
        create_field()
        player_1_turn()


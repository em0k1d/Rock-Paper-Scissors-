from random import randint

def user_interface(options):

    for index,option in enumerate(options):
        print(f'{index} = {option}')

    user_input = int(input('Что ты выберешь: '))
    return user_input


def computer_choice(content):

    computer_chose = randint(0,len(content)-1)
    return computer_chose
    

def check_results(choices, player, computer):

    if player == computer:
        return ('Это Ничья \n')
    elif (player == 0 and computer == len(choices)-1) or (player>computer and not(player==len(choices)-1 and computer==0)):
        return ('Ты выиграл :)\n')
    return ('Ты проиграл :( \n')


def play():
    print('''
    ____________________________________________
    Добро пожаловать в: Камень, Бумага, Ножницы.
    Выбери свое оружие.
    ''')

    options_list = ['Камень', 'Бумага' , 'Ножницы']
    player_result = user_interface(options_list)
    computer_result = computer_choice(options_list)
    
    print(f'  Ты выбрал: {options_list[player_result]}')
    print(f'  Компьютер выбрал: {options_list[computer_result]}')

    results = check_results(options_list,player_result,computer_result)
    print (f'\n{results}')

def main():

    play_again = ''
    while play_again.lower() != 'n':
        play()
        print (f'Хочешь сыграть еще?\n')
        play_again = input('Нажми \'y\' если да, или \'n\' если нет: ')

main()
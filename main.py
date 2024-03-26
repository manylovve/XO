size = 3
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def draw_board():
    print('_' * 4 * size)
    for i in range(size):
        print((' ' * 3 + '|') * 3)
        print('', board[i*3], '|', board[1+i*3], '|', board[2+i*3],'|')
        print(('_' * 3 + '|') * 3)
draw_board()

def game_step(index, char):
    index = int(index)
    if (index > 9 or index < 1 or board[index - 1] in ('X','О')):
        return False
    board[index-1] = char
    return True

def check():
    win=False
    win_combination = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7,), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    )
    for pos in win_combination:
        if (board[pos[0]] == board[pos[1]] == board[pos[2]]):
            win = True
    return win

def start_game():
    player_X = 'X'
    player_O = 'O'
    step = 1

    while ((step < 10)):
        visited = []
        if step % 2 == 1:
            index = input('Ход игрока '+ player_X + ' Введите номер поля: ')
            if index == '0':
                print('Игрок ' + player_X + ' проиграл.')
                break
            if (game_step(index, player_X)) and (index not in visited):
                draw_board()
                visited+=index
                step += 1
            else:
                print('Выберите другую клетку')
            if check():
                print('Выиграл игрок '+ player_X)
                break

        else:
            index = input('Ход игрока ' + player_O + ' Введите номер поля: ')
            if index == '0':
                print('Игрок ' + player_O + ' проиграл.')
                break
            if (game_step(index, player_O)) and (index not in visited):
                draw_board()
                visited += index
                step += 1

            else:
                print('Выберите другую клетку')
            if check():
                print('Выиграл игрок '+ player_O)
                break
        if step == 10:
            print('Ничья')






print('Давай играть!')
start_game()
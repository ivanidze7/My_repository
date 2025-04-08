#Создаем игровое поле(матрицу 3х3)
board = [
    ['*', '*', '*'],
    ['*', '*', '*'],
    ['*', '*', '*']
]

#Функция вывода игрового поля на экран
def print_board(board):
    for row in board:
        for cell in row:
            print(cell, end = '')
        print()

#Функция проверки выиграша(строки, столбцы, диагонали)
def check_win(board, player):
    for row in board:
        if row.count(player) == 3:
            return True
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        return True

#Указываем, что первым ходит "Х"
current_player = 'X'

#Основной цикл игры
while True:
    print_board(board)
    print('Ход игрока', current_player)
    row = int(input('Введите номер строки: ')) - 1
    cell = int(input('Введите номер столбца: ')) - 1

    #Проверяем не занята ли ячейка
    if board[row][cell] != '*':
        print('Ячейка занята')
        continue
    #Осуществляем ход игрока
    board[row][cell] = current_player


    if check_win(board, current_player):
        print_board(board)
        print(f'Игрок {current_player} выиграл!')
        break

    #В случае если никто не победил, а все ячейки заняты, выводим сообщение о ничье
    if all([cell != '*' for row in board for cell in row]):
        print('Ничья')
        print_board()
        break

    #Осуществляем смену игрока
    current_player = '0' if current_player == 'X' else 'X'




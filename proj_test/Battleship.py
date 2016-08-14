# Импорт функции randint из библиотеки random.
from random import randint
# Объявление пустого списка с именем board
board = []
# Создание пяти строк, по пять ячеек в каждой, заполненных как ["O", "O", "O", "O", "O"]
for x in range(5):
    board.append(["O"] * 5)
# Определение функции print_board(), которая через строчный метод .join объединит
# все пять “O” в целую строку, ликвидировав запятые и кавычки, которые мы видим при # выводе строки на экран.
def print_board(board):
    for row in board:
        print (" ".join(row))
print ("Let's play Battleship!")
print_board(board)
# Определение ф-ции, которая будет случайным образом генерировать координату
# игрового корабля по горизонтали.
def random_row(board):
    return randint(0, len(board) - 1)
# Определение ф-ции, которая будет случайным образом генерировать координату
# игрового корабля по вертикали.
def random_col(board):
    return randint(0, len(board[0]) - 1)
# Вызов ф-ций для генерации случайных координат игрового корабля.
ship_row = random_row(board)
ship_col = random_col(board)
print (ship_row)
print (ship_col)
# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
# Поскольку игрок должен иметь 4 попытки, мы осуществляем 4-кратный проход по циклу.
for turn in range(4):
    print ("Turn", turn + 1)
    # Предлагаем игроку угадать координаты по горизонтали и по вертикали.
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))
    # Поясняем условия выигрыша. В случае победы завершаем работу программы.
    if guess_row == ship_row and guess_col == ship_col:
        print ("Congratulations! You sunk my battleship!")
        break
    # Поясняем условия в случае отсутствия выигрыша.
    else:
        # Предусматриваем действие на случай, если игрок вышел за рамки игрового поля.
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print ("Oops, that's not even in the ocean.")
        # Предусматриваем сообщение на случай, если игрок попал в ячейку, по которой уже стрелял.
        elif(board[guess_row][guess_col] == "X"):
            print ("You guessed that one already.")
        # Предусматриваем сообщение на остальные случаи отсутствия выигрыша.
        else:
            print ("You missed my battleship!")
    # Предусматриваем завершение игры, если игрок совершил уже 4 попытки.
    if turn == 3:
        print ("Game Over")
        board[guess_row][guess_col] = "X"
    # Print (turn + 1) here!
print_board(board)
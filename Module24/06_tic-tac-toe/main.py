import copy


class Cell:  # TODO Определение класса должно отделяться от остального кода двумя пустыми строками
    busy = 0
    item = ''

    def __init__(self, number_cell):
        self.number_cell = number_cell


class Board:
    def __init__(self):
        self.clear_field = [Cell(i_number) for i_number in range(9)]
        self.field = copy.deepcopy(self.clear_field)

    def info(self):
        separator = '{:^6}'.format('  ')
        empty_line = '| {:<1} | {:<1} | {:<1} |'
        line_1 = '-'*13 + separator + '-'*13
        line_2 = empty_line.format(
            self.field[6].item, self.field[7].item, self.field[8].item) + separator + '| 7 | 8 | 9 |'
        line_3 = empty_line.format(
            self.field[3].item, self.field[4].item, self.field[5].item) + separator + '| 4 | 5 | 6 |'
        line_4 = empty_line.format(
            self.field[0].item, self.field[1].item, self.field[2].item) + separator + '| 1 | 2 | 3 |'
        print(line_1, line_2, line_3, line_4, line_1, sep='\n')


class Player:

    def __init__(self, name, player_item):
        self.name = name
        self.player_item = player_item


class Game:

    def main(self, total_points, player_1, player_2, board):
        answer = input('Хотите начать новую игру? (1)\n'
                       'Или продолжить турнир? (2)\n'
                       'Ответ: ')
        if answer == '1':
            total_points[player_1.name] = 0
            total_points[player_2.name] = 0

        print(player_1.name, ' - ', total_points[player_1.name])
        print(player_2.name, ' - ', total_points[player_2.name])

        board.field = copy.deepcopy(board.clear_field)
        turn = player_1
        board.info()
        for i_turn in range(9):
            make_a_move(turn)
            board.info()
            w_o_c, all_busy = win_or_continue(turn)
            if w_o_c:
                print('Выйграл игрок {}'.format(turn.name))
                total_points[turn.name] += 1
                break
            elif not w_o_c and all_busy == 9:
                print('Ничья!')
                break
            else:
                if turn.name == player_1.name:
                    turn = player_2
                else:
                    turn = player_1
        game.main(total_points, player_1, player_2, board)


def make_a_move(player):
    choice = int(input('Ходит {}. Укажи номер клетки: '.format(player.name))) - 1
    for i_cell in board.field:
        if i_cell.number_cell == choice:
            if i_cell.busy == 0:
                print('Клетка номер {} теперь занята.'.format(i_cell.number_cell + 1))
                i_cell.busy = 1
                i_cell.item = player.player_item
            else:
                print('Клетка номер {} уже занята!. Выбери другую.'.format(i_cell.number_cell))
                make_a_move(player)


def win_or_continue(player):
    winnable_lines = [['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'],
                      ['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'],
                      ['1', '5', '9'], ['3', '5', '7']]
    taken_cells = ''
    all_busy = 0
    w_o_c = 0
    for i_cell in board.field:
        all_busy += i_cell.busy
        if i_cell.item == player.player_item:
            taken_cells += str(i_cell.number_cell + 1)
    for i_list in winnable_lines:
        count = 0
        for i_num in i_list:
            if i_num in taken_cells:
                count += 1
        if count == 3:
            w_o_c = True
    return w_o_c, all_busy


game = Game()
player_1 = Player('Player 1', 'X')
player_2 = Player('Player 2', 'O')
board = Board()
total_points = {player_1.name: 0,
                player_2.name: 0}

game.main(total_points, player_1, player_2, board)




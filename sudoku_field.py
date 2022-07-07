from cell import Cell


class SudokuField:
    """Класс всего поля игры судоку"""

    def __init__(self, input_data):
        self.field = tuple(tuple(Cell(input_data[j][i]) for i in range(9)) for j in range(9))

    def __str__(self):
        field_str = ''
        for i in range(9):
            for j in range(9):
                field_str += str(self.field[i][j]) + ' '
                if j in (2, 5):
                    field_str += '| '
            field_str += '\n'
            if i in (2, 5):
                field_str += '------|-------|------\n'

        return field_str

    def __repr__(self):
        field_str = ''
        for i in range(9):
            field_str += str(self.field[i])

        return field_str

    def get_line(self, line_number):
        return self.field[line_number - 1]

    def get_row(self, row_number):
        return tuple((self.field[x][row_number] for x in range(9)))

    def get_square(self, cell_line=-1, cell_row=-1, square_number=0):
        if square_number == 0:
            line = cell_line // 3
            row = 3 * (cell_row // 3)
        else:
            line = (square_number - 1) // 3
            row = 3 * ((square_number - 1) % 3)

        return tuple((self.field[i + 3 * line][j] for i in range(3) for j in range(row, row + 3)))

    @staticmethod
    def nums_in_area(cells_tuple):
        numbers_in = [int(x) for x in '123456789']
        numbers_out = []
        for i in numbers_in:
            if i not in cells_tuple:
                numbers_out.append(i)

        return set(numbers_in) - set(numbers_out), set(numbers_out)

    def make_applicants(self):
        will_continue = True

        while will_continue:
            break_loop = False
            for line in range(9):
                for row in range(9):
                    if self.field[line][row].value == '_':
                        _, applicants = SudokuField.nums_in_area(self.field[line])
                        applicants -= SudokuField.nums_in_area(self.get_row(row))[0]
                        applicants -= SudokuField.nums_in_area(self.get_square(line, row))[0]

                        if len(applicants) == 1:
                            self.field[line][row].value = applicants.pop()
                            self.field[line][row].applicants = []
                            break_loop = True
                            break
                        self.field[line][row].applicants = list(applicants)
                if break_loop:
                    break
            if not break_loop:
                will_continue = False

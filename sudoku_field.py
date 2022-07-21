from cell import Cell


class SudokuField:
    """Класс всего поля игры судоку"""

    def __init__(self, input_data):
        self.field = tuple(tuple(Cell(input_data[j][i], j, i) for i in range(9)) for j in range(9))
        self.empty_cells = 0
        print(self)
        self.get_empty_cells()

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

    def get_empty_cells(self):
        """Обновляет количество пустых ячеек в поле."""
        self.empty_cells = 0
        for line in self.field:
            for cell in line:
                if cell == '_':
                    self.empty_cells += 1

    def get_row(self, row_number):
        """Возвращает элементы ряда по номеру (1-9)."""
        return tuple((self.field[x][row_number] for x in range(9)))

    def get_square(self, cell_line=None, cell_row=None, square_number=None):
        """Возвращает элементы квадрата по номеру (1-9)."""
        if square_number is None:
            line = cell_line // 3
            row = 3 * (cell_row // 3)
        else:
            line = square_number // 3
            row = 3 * (square_number % 3)

        return tuple((self.field[i + 3 * line][j] for i in range(3) for j in range(row, row + 3)))

    @staticmethod
    def nums_in_area(cells_tuple):
        """Возвращает цифры которые есть и которых нету в блоке."""
        numbers_in = [int(x) for x in '123456789']
        numbers_out = []
        for i in numbers_in:
            if i not in cells_tuple:
                numbers_out.append(i)

        return set(numbers_in) - set(numbers_out), set(numbers_out)

    def make_applicants(self):
        """Находит всех претендентов на пустую клетку и задает ее значение если претендент один."""
        will_continue = True

        while will_continue:
            break_loop = False
            for line in range(9):
                for row in range(9):
                    if self.field[line][row] == '_':
                        if len(self.field[line][row]) == 1:
                            # print(f'1.({self.field[line][row].x + 1}, {self.field[line][row].y + 1}) - {self.field[line][row].applicants} ->')
                            self.field[line][row].value = self.field[line][row].applicants.pop()
                            # print(f'-> {self.field[line][row].applicants}')
                            # print('SOLO' + str(self.field[line]))
                            break_loop = True
                            break

                        else:
                            _, applicants = SudokuField.nums_in_area(self.field[line])
                            applicants -= SudokuField.nums_in_area(self.get_row(row))[0]
                            applicants -= SudokuField.nums_in_area(self.get_square(line, row))[0]

                            if len(applicants) == 1:
                                # print(f'2.({self.field[line][row].x + 1}, {self.field[line][row].y + 1}) - {applicants} ->')
                                self.field[line][row].value = applicants.pop()
                                self.field[line][row].applicants = set()
                                # print(f'-> {self.field[line][row].applicants}')
                                # print('SOLO' + str(self.field[line]))
                                break_loop = True
                                break
                            if len(self.field[line][row]) == 0 or len(applicants) < len(self.field[line][row]):
                                # print(f'({self.field[line][row].x},{self.field[line][row].y}){self.field[line][row].applicants} -> {applicants}')
                                # print(f'3.({self.field[line][row].x + 1}, {self.field[line][row].y + 1}) - {self.field[line][row].applicants} ->')
                                self.field[line][row].applicants = applicants
                                # print(f'-> {self.field[line][row].applicants}')

                if break_loop:
                    break
            if not break_loop:
                will_continue = False
        self.get_empty_cells()

    @staticmethod
    def delete_applicants(cells_tuple, applicants):
        """Удаляет пересекающихся претендентов."""
        for cell in cells_tuple:
            if cell == '_':
                if len(cell.applicants - applicants) != 0 and len(cell.applicants & applicants) != 0:
                    # print(f'4.({cell.x+1}, {cell.y+1}) - {cell.applicants} -> {applicants}')
                    cell.applicants -= applicants
                    # print(f'-> {cell.applicants}')

    @staticmethod
    def find_naked_couples(cells_tuple):
        """Поиск Голых Пар."""
        if len(SudokuField.nums_in_area(cells_tuple)[1]) > 2:
            for cell1_num in range(9):
                if len(cells_tuple[cell1_num]) == 2:
                    for cell2 in cells_tuple[cell1_num+1:]:
                        if cells_tuple[cell1_num].applicants == cell2.applicants:
                            SudokuField.delete_applicants(cells_tuple, cell2.applicants)

    @staticmethod
    def find_naked_threes(cells_tuple):
        """Поиск Голых Троек."""
        if len(SudokuField.nums_in_area(cells_tuple)[1]) > 3:
            for cell1_num in range(9):
                cell1 = cells_tuple[cell1_num]
                if len(cell1) == 3:
                    for cell2_num in range(cell1_num + 1, 9):
                        cell2 = cells_tuple[cell2_num]
                        if len(cell2) in (2, 3) and len(cell2) == len(cell1.applicants & cell2.applicants):
                            for cell3 in cells_tuple[cell2_num+1:]:
                                if len(cell3) in (2, 3) and len(cell3) == len(cell1.applicants & cell3.applicants):
                                    # print(cells_tuple)
                                    # appl = ''
                                    # for i in cells_tuple:
                                    #     appl += str(i.applicants)
                                    # print(appl)
                                    # print(cell1.applicants)
                                    SudokuField.delete_applicants(cells_tuple, cell1.applicants)

                elif len(cell1) == 2:
                    applicants = cell1.applicants
                    for cell2_num in range(cell1_num + 1, 9):
                        cell2 = cells_tuple[cell2_num]
                        if len(cell2) == 2 and len(applicants & cell2.applicants) in (1, 2):
                            applicants |= cell2.applicants  # 2 or 3
                            for cell3 in cells_tuple[cell2_num+1:]:
                                if len(cell3) == 2 and len(applicants | cell3.applicants) == 3:
                                    applicants |= cell3.applicants
                                    SudokuField.delete_applicants(cells_tuple, applicants)
                                elif len(cell3) == 3 and len(applicants) == len(applicants & cell3.applicants):
                                    applicants = cell3.applicants
                                    SudokuField.delete_applicants(cells_tuple, applicants)

                        elif len(cell2) == 3 and len(cell1.applicants & cell2.applicants) == 2:
                            applicants = cell2.applicants
                            for cell3 in cells_tuple[cell2_num+1:]:
                                if len(cell3) in (2, 3) and len(cell3) == len(applicants & cell3.applicants):
                                    SudokuField.delete_applicants(cells_tuple, applicants)

    def delete_naked_applicants(self, method):
        """Очистка голых претендентов."""
        will_continue = True
        while will_continue:
            num_before = self.empty_cells
            for i in range(9):
                method(self.field[i])
            self.make_applicants()
            for i in range(9):
                method(self.get_row(i))
            self.make_applicants()
            for i in range(9):
                method(self.get_square(square_number=i))
            self.make_applicants()

            self.get_empty_cells()
            if num_before == self.empty_cells:
                will_continue = False

    @staticmethod
    def get_empty_cells_tuple(cells_tuple):
        return set(x for x in cells_tuple if x != '_')


    @staticmethod
    def find_hidden_couples(cells_tuple):
        """Поиск скрытых пар в области."""
        empty_cells = SudokuField.get_empty_cells_tuple(cells_tuple)
        if len(empty_cells) > 2:
            for cell1_num in range(len(empty_cells) - 1):
                for cell2_num in range(cell1_num+1, len(empty_cells)):








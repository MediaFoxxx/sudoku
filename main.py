import time

from sudoku_field import SudokuField


input_easy = (
    '090000080',
    '400000100',
    '000064020',
    '008210000',
    '001030000',
    '957000000',
    '000500000',
    '800700009',
    '000001507'
)


def main(new_field):
    print('Простая проверка чтобы убрать простые варианты:')
    new_field.make_applicants()
    print(new_field)
    print(new_field.empty_cells)

    print('Проверка голых претендентов\n')
    print('Убираем пары:')
    new_field.delete_naked_applicants(SudokuField.find_naked_couples)
    print(new_field)
    print(new_field.empty_cells)
    print('Убираем тройки:')
    new_field.delete_naked_applicants(SudokuField.find_naked_threes)
    print(new_field)
    print(new_field.empty_cells)


if __name__ == '__main__':
    time1 = time.time()
    new_field = SudokuField(input_easy)
    print(new_field.empty_cells)
    for i in range(5):
        main(new_field)
    time2 = time.time()
    print(time2 - time1)

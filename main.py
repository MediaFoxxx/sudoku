from sudoku_field import SudokuField


input_easy = (
    '071000900',
    '006008003',
    '340600050',
    '102900000',
    '000030009',
    '508000700',
    '000080300',
    '600050097',
    '007300068'
)


new_field = SudokuField(input_easy)
print(new_field)
new_field.make_applicants()

print(new_field)
for line in new_field.field:
    for cell in line:
        print(f'{cell.value} - {cell.applicants}')
    print()

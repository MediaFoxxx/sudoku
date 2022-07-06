# input_line = [x for x in list('928037465')]
#
# no_in_input = [x for x in list('123456789') if x not in input_line]
#
# if len(no_in_input) == 1:
#     for i in range(len(input_line)):
#         if input_line[i] == '0':
#             input_line[i] = no_in_input[0]
#             break
#
#
# print(input_line)


input_easy = (
    (0, 6, 0, 0, 0, 0, 4, 2, 0),
    (3, 0, 0, 0, 0, 8, 9, 0, 0),
    (0, 0, 7, 2, 4, 5, 6, 0, 0),
    (9, 0, 6, 3, 0, 4, 0, 0, 0),
    (0, 7, 3, 0, 1, 0, 2, 0, 0),
    (8, 5, 0, 0, 6, 2, 3, 4, 9),
    (0, 0, 4, 1, 2, 0, 0, 9, 8),
    (0, 0, 9, 0, 0, 3, 0, 6, 0),
    (6, 0, 0, 4, 0, 0, 1, 3, 0),
)


for i in range(9):
    line = i // 3
    row = 3 * (i % 3)

    print('Cube number ' + str(i+1))
    for j in range(3):
        print(*input_easy[j+3*line][row:row+3])
    print()


def get_line(line_number):
    pass




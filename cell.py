from bisect import insort
# abv = [1, 12, 23, 112]
# insort(abv, 14)
# print(abv)


class Cell:
    """Класс ячейки поля судоку."""

    def __init__(self, value):
        self.applicants = []
        if value == '0':
            self.value = '_'
        else:
            self.value = int(value)

    def __repr__(self):
        return str(self.value)

    def __eq__(self, other):
        if type(other) == "<class 'cell.Cell'>":
            return self.value == other.value
        else:
            return self.value == other

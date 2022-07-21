class Cell:
    """Класс ячейки поля судоку."""

    def __init__(self, value, x, y):
        self.applicants = set()
        self.x = x
        self.y = y
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

    def __len__(self):
        return len(self.applicants)

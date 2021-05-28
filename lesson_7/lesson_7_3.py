class Cell:
    def __init__(self, param):
        self.param = param

    def __add__(self, second_cell):
        return Cell(self.param + second_cell.param)

    def __sub__(self, second_cell):
        return Cell(abs(self.param - second_cell.param))

    def __mul__(self, second_cell):
        return Cell(self.param * second_cell.param)

    def __truediv__(self, second_cell):
        if self.param > second_cell.param:
            return Cell(round(self.param / second_cell.param))
        else:
            return Cell(round(second_cell.param / self.param))

    def make_order(self, n):
        order_str = ''
        for i in range(self.param):
            if i % n == 0:
                order_str += '\n*'
            else:
                order_str += '*'
        return order_str


c1 = int(input("Введите количество ячеек в первой клетке: "))
c2 = int(input("Введите количество ячеек во второй клктке: "))
n = int(input("Введите количество ячеек в ряду: "))
mc1 = Cell(c1)
mc2 = Cell(c2)
print(f"При сложении получится клетка, в которой {(mc1 + mc2).param} ячееек.")
if c1 == c2:
    print("У клетках одинаковое количество ячеек. При вычитании клетки исчезнут.")
else:
    print(f"При вычитании получится клетка, в которой {(mc1 - mc2).param} ячееек.")
print(f"При умножении получится клетка, в которой {(mc1 * mc2).param} ячееек.")
print(f"При делении получится клетка, в которой {(mc1 / mc2).param} ячееек.\n")
print(f"Первая клетка выглядит так:")
print(mc1.make_order(n))
print(f"\nВторая клетка выглядит так:")
print(mc2.make_order(n))

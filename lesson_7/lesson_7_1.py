class Matrix:

    def __init__(self, param):
        self.param = param

    def __getitem__(self, index):
        return self.param[index]

    def __str__(self):
        return f"{self.param[0]}\n{self.param[1]}\n{self.param[2]}"

    def __add__(self, param):
        summ_param = [[], [], []]
        for i in range(3):
            for j in range(3):
                summ_param[i].append(self[i][j] + param[i][j])
        return Matrix(summ_param)


my_list_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
my_list_2 = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
mc1 = Matrix(my_list_1)
mc2 = Matrix(my_list_2)

print(f"Первая матрица\n{mc1}\n")
print(f"Вторая матрица\n{mc2}\n")
print(f"Сумма матриц\n{mc1 + mc2}")

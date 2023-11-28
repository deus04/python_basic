import copy
class Matrix:
    data = []   #TODO возожно тут нужно создавать пустой шаблон матрицы х на у,
                # но непойму можно ли создать параметр data в __init_
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # data = [[0 for i_elem in range(x)] for j_elem in range(y)]
    def add(self, m2):
        copy_matrix = copy.deepcopy(self.data)
        for i_row in copy_matrix:
            for i_item in i_row:
                copy_matrix[copy_matrix.index(i_row)][i_row.index(i_item)] += m2.data[copy_matrix.index(i_row)][i_row.index(i_item)]
        return copy_matrix

    def subtract(self, m2):
        copy_matrix = copy.deepcopy(self.data)
        for i_row in copy_matrix:
            for i_item in i_row:
                copy_matrix[copy_matrix.index(i_row)][i_row.index(i_item)] -= m2.data[copy_matrix.index(i_row)][i_row.index(i_item)]
        return copy_matrix

    def multiply(self,m3):
        mult_matrix = Matrix(self.x, m3.y)
        for i_elem in range(self.x):
            mult_matrix.data.append(list(range(m3.y)))
            for j_elem in range(m3.y):
                mult_matrix.data[i_elem][j_elem] = self.data[i_elem][0] * m3.data[0][j_elem] + self.data[i_elem][1] * m3.data[1][j_elem] + self.data[i_elem][2] * m3.data[2][j_elem]
        return mult_matrix.data

    def transpose(self):
        tmatrix = []
        for i_elem in range(self.y):
            tmatrix.append(list(range(self.x)))
            for j_elem in range(self.x):
                tmatrix[i_elem][j_elem] = self.data[j_elem][i_elem]
        return tmatrix


# Примеры работы с классом:



# Создание экземпляров класса Matrix
m1 = Matrix(2, 3)
m1.data = [[1, 2, 3],
           [4, 5, 6]]


m2 = Matrix(2, 3)
m2.data = [[7, 8, 9],
           [10, 11, 12]]


# Тестирование операций
print("Матрица 1:")
print(m1.data)

print("Матрица 2:")
print(m2.data)

print("Сложение матриц:")
print(m1.add(m2))

print("Вычитание матриц:")
print(m1.subtract(m2))

m3 = Matrix(3, 2)
m3.data = [[1, 2], [3, 4], [5, 6]]

print("Умножение матриц:")
print(m1.multiply(m3))

print("Транспонирование матрицы 1:")
print(m1.transpose())


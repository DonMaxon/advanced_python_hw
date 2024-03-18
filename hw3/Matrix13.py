from typing import Tuple, Any
from copy import deepcopy


class HashMixin:

    def __hash__(self):
        return self.matrix[0][0]

class Matrix(HashMixin):
    def __init__(self, data: Tuple[Tuple[Any]]):
        self.rows = len(data)
        self.cols = len(data[0])
        self.matrix = deepcopy(data)

    def __add__(self, other):
        if self.rows !=  other.rows or self.rows !=  other.rows:
            raise ValueError("Matrices must to have the same dimensions to add")
        result = deepcopy(self)
        for i in range(self.rows):
            for j in range(self.cols):
                result.matrix[i][j] += other.matrix[i][j]
        return result

    def __matmul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Number of columns of the first matrix must to be equal to the number of rows of the second matrix")
        result = Matrix.__create_null_matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return result


    def __mul__(self, other):
        result = deepcopy(self)
        if self.rows !=  other.rows or self.rows !=  other.rows:
            raise ValueError("Matrices must to have the same dimensions to add")
        for i in range(self.rows):
            for j in range(self.cols):
                result.matrix[i][j] *=other.matrix[i][j]
        return result

    @staticmethod
    def __create_null_matrix(rows, cols):
        return Matrix([[0 for i in range(cols)] for _ in range(rows)])

    def __str__(self):
        return str(self.matrix)
import numpy as np
np.ndarray
from Matrix13 import Matrix
from Matrix2 import NumpyMatrix
arr1 = np.random.randint(0, 10, (10, 10))
arr2 = np.random.randint(0, 10, (10, 10))
matrix1 = Matrix(arr1)
matrix2 = Matrix(arr2)
npmatrix1 = NumpyMatrix(arr1)
npmatrix2 = NumpyMatrix(arr2)

with open('artifacts/matrix1.txt', 'w') as f:
    f.write(str((matrix1)))
with open('artifacts/matrix2.txt', 'w') as f:
    f.write(str((matrix2)))
with open('artifacts/matrix+.txt', 'w') as f:
    f.write(str((matrix1+matrix2)))
with open(r'artifacts/matrix_matmul.txt', 'w') as f:
    f.write(str((matrix1*matrix2)))
with open('artifacts/matrix_mul.txt', 'w') as f:
    f.write(str((matrix1 @ matrix2)))

A = Matrix(((5, 0), (0, 5)))
B = Matrix(((1, 1), (1, 1)))
C = Matrix(((5, 4), (11, 5)))
D = Matrix(((1, 1), (1, 1)))
with open('artifacts/A.txt', 'w') as f:
    f.write(str(A))
with open('artifacts/B.txt', 'w') as f:
    f.write(str(B))
with open('artifacts/C.txt', 'w') as f:
    f.write(str(C))
with open('artifacts/D.txt', 'w') as f:
    f.write(str(D))
with open('artifacts/AB.txt', 'w') as f:
    f.write(str(A@B))
with open(r'artifacts/CD.txt', 'w') as f:
    f.write(str(C@D))
with open(r'artifacts/hash.txt', 'w') as f:
    f.write(str(hash(A@B))+'\n')
    f.write(str(hash(C@D)))

with open('artifacts/npmatrix1.txt', 'w') as f:
    f.write(str((npmatrix1).value))
with open('artifacts/npmatrix2.txt', 'w') as f:
    f.write(str((npmatrix2).value))
with open('artifacts/npmatrix+.txt', 'w') as f:
    f.write(str((npmatrix1 + npmatrix2)))
with open(r'artifacts/npmatrix_matmul.txt', 'w') as f:
    f.write(str((npmatrix1 * npmatrix2)))
with open(r'artifacts/npmatrix_mul.txt', 'w') as f:
    f.write(str((npmatrix1 @ npmatrix2)))


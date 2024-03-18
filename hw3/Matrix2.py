import numpy as np
from typing import List, Any
from copy import deepcopy


class NumpyMatrix(np.lib.mixins.NDArrayOperatorsMixin):

    def __init__(self, value: List[List[Any]]):
        self.value = np.asarray(value)

    @property
    def value(self):
        return self._value

    def __str__(self):
        return np.array2string(self.value, precision=2, separator=', ',
                      suppress_small=True)

    @value.setter
    def value(self, value):
        self._value = value

    def savetxt(self, path):
        np.savetxt(path, self.value, fmt='%1.4e')

    def __add__(self, other):
        return self.value+other.value

    def __mul__(self, other):
        return self.value*other.value

    def __matmul__(self, other):
        return self.value@other.value

    def __sub__(self, other):
        return self.value-other.value


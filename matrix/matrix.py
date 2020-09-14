class Matrix(object):
    def __init__(self, matrix_string):
        self.mat = [[int(x) for x in line.split(" ")] for line in matrix_string.split('\n')]
        self.mat_transposed = [*zip(*self.mat)]

    def row(self, index):
        return self.mat[index]

    def column(self, index):
        return self.mat_transposed[index]

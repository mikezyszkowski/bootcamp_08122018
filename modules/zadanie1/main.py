from mathematica.algebra import matrices

a = [[1, 2], [10, 10]]
b = [[2, 3], [5, 6]]

c = matrices.add_matrices(a, b)

print(c)
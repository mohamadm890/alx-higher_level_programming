#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    list_res = []
    for row in matrix:
        squared_row = list(map(lambda x: x**2, row))
        list_res.append(squared_row)
    return list_res

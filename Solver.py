import numpy as np
import random

def check_constraints(sudoku, number, row, column):
    if number not in sudoku[row, :]:
        if number not in sudoku[:,column]:
            rowStart, rowEnd = (0, 3) if row <= 2 else (3,6) if 3 <= row <= 5 else (6,9)
            colStart, colEnd = (0, 3) if column <= 2 else (3, 6) if 3 <= column <= 5 else (6, 9)
            reducedSudoku = sudoku[rowStart:rowEnd, colStart:colEnd]
            if number not in reducedSudoku:
                return True
    return False

def reduce_domain(sudoku, domain, row, column):
    domain = list(filter((lambda x: check_constraints(sudoku, x, row, column) == True) , domain))
    return domain

def get_next_pos(row, column):
    column = column + 1 if column < 8 else 0
    row = row + 1 if column == 0 else row

    return (row, column)

def solve(sudoku):
    return sudokuSolver(sudoku, row=0, column=0)

def sudokuSolver(sudoku, row, column):
    if row < 9:
        domain = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if sudoku[row][column] == 0:
            domain = reduce_domain(sudoku, domain, row, column)

            nextSudoku = None
            while nextSudoku is None:
                if len(domain) > 1:
                    value = domain[random.randint(0, len(domain)-1)]
                elif len(domain) == 1:
                    value = domain[0]
                else:
                    return None

                domain.remove(value)
                nextSudoku = sudoku.copy()
                nextSudoku[row][column] = value
                nextRow, nextColumn = get_next_pos(row, column)
                nextSudoku = sudokuSolver(nextSudoku, nextRow, nextColumn)
            return nextSudoku
        else:
            row, column = get_next_pos(row, column)
            nextSudoku = sudokuSolver(sudoku, row, column)
            return nextSudoku
    else:
        return sudoku

def test(sudoku):
    lista = []
    for i in range(9):
        for j in range(9):
            lista.append(check_constraints(sudoku, sudoku[i][j], i, j))

    print(not all(lista))


sudoku = np.array([
          [0, 0, 4, 3, 0, 0, 2, 0, 9],
          [0, 0, 5, 0, 0, 9, 0, 0, 1],
          [0, 7, 0, 0, 6, 0, 0, 4, 3],
          [0, 0, 6, 0, 0, 2, 0, 8, 7],
          [1, 9, 0, 0, 0, 7, 4, 0, 0],
          [0, 5, 0, 0, 8, 3, 0, 0, 0],
          [6, 0, 0, 0, 0, 0, 1, 0, 5],
          [0, 0, 3, 5, 0, 8, 6, 9, 0],
          [0, 4, 2, 9, 1, 0, 3, 0, 0]])

print(solve(sudoku))
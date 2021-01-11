import argparse
from mip import BINARY, Model, xsum
from sudokudata import SudokuData
from sys import stdout as out
from sys import argv

def solve(args):
    inst = SudokuData(args.file)
    numbers = inst.numbers
    m = Model()

    # define 3D boolean matrix where k defines the value
    x = [[[m.add_var(var_type=BINARY)
            for j in range(9)]
                for i in range(9)]
                    for k in range(9)]

    # fixed values constraints
    for i in range(9):
        for j in range(9):
            for k in range(9):
                if numbers[i][j][k] == 1:
                    m += x[i][j][k] == 1

    # exactly 1 value per cell
    for i in range(9):
        for j in range(9):
            m+=xsum(x[i][j][k] for k in range(9)) == 1

    # numbers 1-9 in each row
    for i in range(9):
        for k in range(9):
            m += xsum(x[i][j][k] for j in range(9)) == 1

    # numbers 1-9 in each column
    for j in range(9):
        for k in range(9):
            m += xsum(x[i][j][k] for i in range(9)) == 1
            
    # numbers 1-9 in each block  
    for i2 in range(3):
        for j2 in range(3):
            for k in range(9):
                m += xsum(x[i][j][k]
                    for i in range(i2*3,i2*3+3)
                        for j in range(j2*3, j2*3+3)) == 1

    if args.diagonal:
        for k in range(9):
            m += xsum(x[i][i][k] for i in range(9)) == 1
            m += xsum(x[i][8 - i][k] for i in range(9)) == 1

    if args.antiking:
        king_moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for i in range(9):
            for j in range(9):
                for move in king_moves:
                    if i + move[0] not in list(range(9)) or j + move[1] not in list(range(9)):
                        continue
                    else:
                        for k in range(9):
                            m += x[i][j][k] + x[i+move[0]][j+move[1]][k] <= 1

    if args.antiknight:
        knight_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        for i in range(9):
            for j in range(9):
                for move in knight_moves:
                    if i + move[0] not in list(range(9)) or j + move[1] not in list(range(9)):
                        continue
                    else:
                        for k in range(9):
                            m += x[i][j][k] + x[i+move[0]][j+move[1]][k] <= 1

    if args.anticonsecutive:
        orthog_adjacent = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        for i in range(9):
            for j in range(9):
                for move in orthog_adjacent:
                    if i + move[0] not in list(range(9)) or j + move[1] not in list(range(9)):
                        continue
                    else:
                        for k in range(9):
                            if k == 0:
                                m += x[i][j][k] + x[i+move[0]][j+move[1]][k+1] <= 1
                            elif k == 8:
                                m += x[i][j][k] + x[i+move[0]][j+move[1]][k-1] <= 1
                            else:
                                m += x[i][j][k] + x[i+move[0]][j+move[1]][k-1] <= 1
                                m += x[i][j][k] + x[i+move[0]][j+move[1]][k+1] <= 1

    m.optimize()

    return x


def print_solution(x):
    try:
        for i in range(9):
            for j in range(9):
                for k in range(9):
                        if x[i][j][k].x >= 0.99:
                            out.write(str(k+1))
                out.write(" ")
            out.write("\n")
        out.write("\n\n")
    except TypeError:
        print("\n\nNo solution could be found.\n\n")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    parser.add_argument("-an", "--antiknight", default=False, action="store_true", help="anti-knight sudoku rules apply")
    parser.add_argument("-ak", "--antiking", default=False, action="store_true", help="anti-king sudoku rules apply")
    parser.add_argument("-d", "--diagonal", default=False, action="store_true", help="diagonal sudoku rules apply")
    parser.add_argument("-ac", "--anticonsecutive", default=False, action="store_true", help="orthogonally adjacent cells must not contain consecutive digits")
    args = parser.parse_args()
    print(args)
    print_solution(solve(args))

if __name__ == "__main__":
    main()
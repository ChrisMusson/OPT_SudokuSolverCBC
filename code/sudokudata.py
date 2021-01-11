class SudokuData:
    #reads sudoku.txt into a 3D boolean matrix
    def __init__(self, filename : str):
        self.numbers = [[[0 for i in range(9)] for j in range(9)] for k in range(9)] 

        f = open(filename, 'r')
        line_num = 0
        for line in f:
            vals = line.strip().split(' ')
            for i, val in enumerate(vals):
                if val != "*":
                    self.numbers[line_num][i][int(val.strip())-1] = 1
            line_num += 1

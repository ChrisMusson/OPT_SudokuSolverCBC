class SudokuData:
    #reads sudoku.txt into a 3D boolean matrix
    def __init__(self, filename, killer):
        self.numbers = [[[0 for i in range(9)] for j in range(9)] for k in range(9)] 

        with open(filename) as f:
            head = [next(f).strip() for x in range(9)]
            tail = []
            while True:
                try:
                    tail.append(next(f).strip())
                except StopIteration:
                    break
        
        for i, line in enumerate(head):
            vals = line.split(' ')
            for j, val in enumerate(vals):
                if val != "*":
                    self.numbers[i][j][int(val.strip()) - 1] = 1

        if killer:
            layout = ""
            for line in tail:
                if line != "":
                    layout += line
            self.killer_layout = layout.split(",")

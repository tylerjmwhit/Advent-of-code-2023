
import numpy as np

def testadjacent(start: int, size: int, row: int, matrix, symbols ) -> int:
    #grabbing the number
    stop = start+size
    number = matrix[row][start:stop]
    print(number)
    x_number = int("".join(matrix[row][start:stop]))
    x_row = len(matrix[row])-1

    # testing before
    before = max(start-1, 0)
    charc = matrix[row][before]
    if before != 0 and charc in symbols:
        return x_number
    # testing after
    after = min(stop, x_row)
    charc = matrix[row][after]
    if after != x_row and charc in symbols:
        return x_number
    #testing above
    if row !=0:
        for i in range(before, after+1):
            charc = matrix[row-1][i]
            if charc in symbols:
                return x_number
    #testing below
    if row != len(matrix)-1:
        for i in range(before,after+1):
            charc = matrix[row+1][i]
            if charc in symbols:
                return x_number
    return 0


if __name__ == "__main__":
    matrix = []
    with open(r"Day_3\example1.txt") as file:
        for line in file:
            matrix.append(list(line.strip()))
    
    unique = np.unique(matrix)
    excluded = np.array([1,2,3,4,5,6,7,8,9,'.'])
    symbols = np.setdiff1d(unique,excluded)
    
    #find the size of the number
    size = 0
    sum = 0
    for row, line in enumerate(matrix):
        for y , charc in enumerate(line):
            y_len = len(line)-1
            if charc.isdecimal():
                size +=1
            elif not charc.isdecimal() and size == 0:
                continue
            elif not charc.isdecimal() and size > 0:
                # end of the number was found
                start = max(y - size , 0)
                sum += testadjacent(start,size,row,matrix, symbols)
                size = 0
                continue
            if y == y_len and size > 0:
                start = max(y+1 - size , 0)
                sum += testadjacent(start,size,row,matrix, symbols)
                size = 0
    print(sum)
        
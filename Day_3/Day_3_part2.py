def gearRatio(row: int, col: int, matrix) -> int:
    num = []
    num_str = ''
    row_len = len(matrix[row]) -1
    #testing before
    before = max(col-1,0)
    test_char = matrix[row][before]
    if test_char.isdecimal():
        while test_char.isdecimal() and before >= 0:
            num_str = test_char + num_str
            before -= 1
            test_char = matrix[row][before]
        num.append(int(num_str))
        num_str = ''
    
    #testing after
    after = min(col+1, row_len)
    test_char = matrix[row][after]
    if after != row_len and test_char.isdecimal():
        while test_char.isdecimal() and after <= row_len:
            num_str += test_char
            after += 1
            test_char = matrix[row][after]
        num.append(int(num_str))
        num_str = ''

    #testing above
    if row!=0:
        #if directly above is a number
        before = max(col-1,0)
        after = min(col+1, row_len)
        test_char = matrix[row-1][col]
        if test_char.isdecimal():
            num_str = test_char
            test_char = matrix[row-1][before]
            while test_char.isdecimal() and before >=0:
                num_str = test_char + num_str
                before -= 1
                test_char = matrix[row-1][before]
            test_char = matrix[row-1][after]
            while test_char.isdecimal() and after <= row_len:
                num_str += test_char
                after += 1
                test_char = matrix[row-1][after]
            num.append(int(num_str))
            num_str = ''
        else:
            #testing if to the left is a number
            if matrix[row-1][before].isdecimal():
                test_char = matrix[row-1][before]
                while test_char.isdecimal() and before >= 0:
                    num_str = test_char + num_str
                    before -= 1
                    test_char = matrix[row-1][before]
                num.append(int(num_str))
                num_str = ''

            #testing if to the right is a number
            if matrix[row-1][after].isdecimal():
                test_char = matrix[row-1][after]
                while test_char.isdecimal() and after <= row_len:
                    num_str += test_char
                    after += 1
                    if after <= row_len:
                        test_char = matrix[row-1][after]
                num.append(int(num_str))
                num_str = ''
    #testing below
    if row!= len(matrix)-1:
        #if directly above is a number
        before = max(col-1,0)
        after = min(col+1, row_len)
        test_char = matrix[row+1][col]
        if test_char.isdecimal():
            num_str = test_char
            
            test_char = matrix[row+1][before]
            while test_char.isdecimal() and before >=0:
                num_str = test_char + num_str
                before -= 1
                test_char = matrix[row+1][before]
            
            test_char = matrix[row+1][after]
            while test_char.isdecimal() and after <= row_len:
                num_str += test_char
                after += 1
                test_char = matrix[row+1][after]
            num.append(int(num_str))
            num_str = ''
        else:
            #testing if to the left is a number
            if matrix[row+1][before].isdecimal():
                test_char = matrix[row+1][before]
                while test_char.isdecimal() and before >= 0:
                    num_str = test_char + num_str
                    before -= 1
                    test_char = matrix[row+1][before]
                num.append(int(num_str))
                num_str = ''

            #testing if to the right is a number
            if matrix[row+1][after].isdecimal():
                test_char = matrix[row+1][after]
                while test_char.isdecimal() and after <= row_len:
                    num_str += test_char
                    after += 1
                    test_char = matrix[row+1][after]
                num.append(int(num_str))
                num_str = ''
    print(num)
    if len(num) == 2:
        return num[0] * num[1]
    return 0
    






if __name__ == "__main__":
    matrix = []
    with open(r"Day_3\input1.txt") as file:
        for line in file:
            matrix.append(list(line.strip()))


    sum = 0
    for row, line in enumerate(matrix):
        for col , charc in enumerate(line):
            if charc == '*':
                sum += gearRatio(row,col,matrix)
    print(sum)
            
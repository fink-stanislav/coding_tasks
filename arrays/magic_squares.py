
def check_if_magic(matrix):
    row_sums = []
    col_sums = []
    diag_sums = []
    
    size = len(matrix[0])
    for j in range(0, size):
        row_sum = 0
        for i in range(0, size):
            row_sum += matrix[j][i]
        row_sums.append(row_sum)
            

def convert_to_magic_square(matrix):
    pass
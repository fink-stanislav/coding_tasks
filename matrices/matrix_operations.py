# An Inplace function to rotate 
# N x N matrix by 90 degrees in
# anti-clockwise direction
def rotate_matrix(mat):
    N = len(mat)
    M = len(mat[0])
    if N != M:
        raise ValueError('Matrix should be square. Dimensions: {}x{}'.format(str(M), str(N)))

    # Consider all squares one by one
    for x in range(0, int(N/2)):

        # Consider elements in group   
        # of 4 in current square
        for y in range(x, N-x-1):

            # store current cell in temp variable
            temp = mat[x][y]

            # move values from right to top
            mat[x][y] = mat[y][N-1-x]

            # move values from bottom to right
            mat[y][N-1-x] = mat[N-1-x][N-1-y]

            # move values from left to bottom
            mat[N-1-x][N-1-y] = mat[N-1-y][x]

            # assign temp to left
            mat[N-1-y][x] = temp

# Function to pr the matrix
def display_matrix( mat ):
    N = len(mat)
    M = len(mat[0])

    if N != M:
        raise ValueError('Matrix should be square. Dimensions: {}x{}'.format(str(M), str(N)))

    for i in range(0, N):
        print(' '.join(str(mat[i])))

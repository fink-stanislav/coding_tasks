def get_subject_coords(grid, subject):
    n = len(grid)
    for y in range(0, n):
        for x in range(0, n):
            if grid[y][x] == subject:
                return [x, y]
    return [-1, -1]

def get_princess_coords(grid):
    return get_subject_coords(grid, 'p')

def get_bot_coords(grid):
    return get_subject_coords(grid, 'm')

def get_coord_to_change(diff_coords):
    if abs(diff_coords[0]) > abs(diff_coords[1]):
        return 'x'
    else:
        return 'y'

def decide_direction(coord_type, diff):
    if coord_type == 'x':
        if diff[0] > 0:
            return 'LEFT'
        else:
            return 'RIGHT'
    else:
        if diff[1] > 0:
            return 'UP'
        else:
            return 'DOWN'

def move_bot(grid, pred, coord_type, direction):
    new_coords = []
    new_coords.append(pred[0])
    new_coords.append(pred[1])
    if coord_type == 'x':
        if direction == 'LEFT':
            new_coords[0] = pred[0] - 1
        else:
            new_coords[0] = pred[0] + 1
    else:
        if direction == 'UP':
            new_coords[1] = pred[1] - 1
        else:
            new_coords[1] = pred[1] + 1
    grid[pred[1]][pred[0]] = '-'
    grid[new_coords[1]][new_coords[0]] = 'm'

def nextMove(n,r,c,grid):
    pc = get_princess_coords(grid)
    bc = get_bot_coords(grid)
    dc = (bc[0] - pc[0], bc[1] - pc[1])
    if pc[0] + pc[1] == -2:
        return False
    coord_type = get_coord_to_change(dc)
    direction = decide_direction(coord_type, dc)
    move_bot(grid, bc, coord_type, direction)
    return direction

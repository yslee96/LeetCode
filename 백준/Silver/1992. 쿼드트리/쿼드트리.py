import sys
input = sys.stdin.readline

def compress(row, col, size, video):

    first_value = video[row][col]
    
    is_same = True
    for i in range(row, row+size):
        for j in range(col, col+size):
            if video[i][j] != first_value:
                is_same = False
                break
        if not is_same:
            break
        
    if is_same:
        return first_value
    
    else:
        half = size // 2
        top_left = compress(row, col, half, video)
        top_right = compress(row, col + half, half, video)
        bottom_left = compress(row+half, col, half, video)
        bottom_right = compress(row+half, col+half, half, video)
        return f'({top_left}{top_right}{bottom_left}{bottom_right})'

size = int(input())
video = [list(input().rstrip()) for _ in range(size)]
result = compress(0, 0, size, video)
print(result)
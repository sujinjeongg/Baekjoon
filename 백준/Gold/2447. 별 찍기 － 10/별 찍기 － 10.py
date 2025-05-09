N = int(input())

def solution(N):
    grid = [[' ' for _ in range(N)] for _ in range(N)]

    def recursion(x, y, size):
        if size==1:
            grid[x][y] = '*'
            return 

        new_size = size//3 
        for i in range(3):
            for j in range(3):
                if i==1 and j==1:
                    continue 
                recursion(x+i*new_size, y+j*new_size, new_size)

    recursion(0, 0, N)
    for row in grid:
        print(''.join(row))

solution(N)
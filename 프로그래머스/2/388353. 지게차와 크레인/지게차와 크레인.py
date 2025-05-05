from collections import deque

def solution(storage, requests):
    N, M = len(storage), len(storage[0])
    grid = [list(row) for row in storage]
    total = N * M

    def is_connected(i, j):
        visited = [[False] * M for _ in range(N)]
        queue = deque()
        queue.append((i, j))
        visited[i][j] = True

        while queue:
            x, y = queue.popleft()
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M:
                    if not visited[nx][ny] and grid[nx][ny] == '-':
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                else:
                    return True
        return False

    for req in requests:
        target = req[0]
        to_remove = []

        if len(req) == 2:
            for i in range(N):
                for j in range(M):
                    if grid[i][j] == target:
                        to_remove.append((i, j))
        else:
            for i in range(N):
                for j in range(M):
                    if grid[i][j] == target and is_connected(i, j):
                        to_remove.append((i, j))

        for x, y in to_remove:
            grid[x][y] = '-'
            total -= 1

    return total

'''def solution(storage, requests):
    storage = [list(row) for row in storage]
    
    dx = (-1,0,1,0)
    dy = (0,-1,0,1)
    
    def out_of_range(x, y):
        return x<0 or y<0 or x>=len(storage) or y>=len(storage[0])
    
    # 사방중 하나라도 비어있으면 지게차 접근 가능 
    def bfs(x, y, request):
        q = deque()
        q.append((x, y))
        
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if out_of_range(nx, ny) or storage[nx][ny] == "-":
                    storage[x][y] = "-"
                    break
                
    for request in requests:
        for i in range(len(storage)):
            for j in range(len(storage[0])):
                if len(request) == 1: # 지게차
                    if storage[i][j] == request:
                        bfs(i, j)
                else: # 크레인 
                    if storage[i][j] == request[0]:
                        storage[i][j] = "-"
                        
    cnt = 0
    for i in range(len(storage)):
            for j in range(len(storage[0])):
                if storage[i][j] != "-":
                    cnt += 1
            
    answer = cnt
    return answer
'''
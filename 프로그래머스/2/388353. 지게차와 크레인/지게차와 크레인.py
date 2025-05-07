def solution(storage, requests):
    from collections import deque
     
    storage = [list(row) for row in storage]
    N = len(storage)
    M = len(storage[0])
    
    dx = (-1,0,1,0)
    dy = (0,-1,0,1)
    
    def out_of_range(x, y):
        return x<0 or y<0 or x>=N or y>=M
    
    def bfs(x, y):
        q = deque()
        q.append((x, y))
        visited = [[False]*M for _ in range(N)]
        visited[x][y] = True
        
        while q:
            sx, sy = q.popleft()
            for i in range(4):
                nx = sx + dx[i]
                ny = sy + dy[i]
                if not out_of_range(nx, ny): # 외부와 연결되지 않은 컨테이너 
                    if not visited[nx][ny] and storage[nx][ny] == '-':
                        q.append((nx, ny))
                        visited[nx][ny] = True
                else: # 외부와 연결된 컨테이너 
                    return True
        return False 
    
    total = N*M
    for rq in requests:
        to_remove = []
        if len(rq) == 1: # 지게차 
            for i in range(N):
                for j in range(M):
                    if storage[i][j] == rq and bfs(i, j):
                        to_remove.append((i, j))
        else: # 크레인
            for i in range(N):
                for j in range(M):
                    if storage[i][j] == rq[0]:
                        to_remove.append((i, j))
                 
        for x, y in to_remove:
            storage[x][y] = '-'
            total -= 1
    
    answer = total
    return answer
from collections import defaultdict

def solution(points, routes):
    # 포인트 번호 → 좌표로 매핑
    point_map = {i + 1: tuple(pt) for i, pt in enumerate(points)}
    
    position_count = defaultdict(int)

    for route in routes:
        time = 0
        cur = point_map[route[0]]
        
        # 출발 위치도 기록해야 함 (0초)
        position_count[(time, cur)] += 1

        for next_point in route[1:]:
            nxt = point_map[next_point]
            r1, c1 = cur
            r2, c2 = nxt
            
            # r 먼저
            dr = 1 if r2 > r1 else -1
            for _ in range(abs(r2 - r1)):
                r1 += dr
                time += 1
                position_count[(time, (r1, c1))] += 1
            
            # c 다음
            dc = 1 if c2 > c1 else -1
            for _ in range(abs(c2 - c1)):
                c1 += dc
                time += 1
                position_count[(time, (r1, c1))] += 1
            
            cur = (r2, c2)
    
    # 충돌 위험 상황 계산
    danger = sum(1 for cnt in position_count.values() if cnt >= 2)
    return danger


'''
def solution(points, routes):
    from collections import deque
    from collections import defaultdict
    
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    
    def out_of_range(x, y):
        return x<0 or y<0 or x>100 or y>100
    
    def bfs(x, y, dstx, dsty):
        visited = [[False] * 101 for _ in range(101)]
        visited[x][y] = True 
        prev_visited = [[None] * 101 for _ in range(101)]
        q = deque()
        q.append((x, y))
        
        while q:
            sx, sy = q.popleft()
            if (sx, sy) == (dstx, dsty):
                break
            for i in range(4):
                nx = sx + dx[i]
                ny = sy + dy[i]
                if not out_of_range(nx, ny) and not visited[nx][ny]:
                    visited[nx][ny] = True
                    prev_visited[nx][ny] = (sx, sy)
                    q.append((nx, ny))
                    
        # 최단 경로 추적
        path = []
        current = (dstx, dsty)
        while current != (x, y):
            path.append(current)
            current = prev_visited[current[0]][current[1]]
        path.append((x, y))
        
        path.reverse()
        
        return path 
    
    # 로봇들의 경로들 저장 
    paths = []
    for route in routes:
        path = []
        for i in range(len(route)-1):
            src = route[i]
            dst = route[i+1]
            segment = bfs(points[src-1][0], points[src-1][1], points[dst-1][0], points[dst-1][1])
            if path:
                segment = segment[1:]  # 중복 방지
            path += segment
        paths.append(path)
    
    # 로봇들의 시간별 위치 저장 (딕셔너리 사용하여 카운트)
    d = defaultdict(lambda: defaultdict(int)) # 이중 구조 : 시간, 위치 -> 카운트 
    max_time = 0
    for path in paths:
        for t, (x, y) in enumerate(path):
            d[t][(x, y)] += 1
            max_time = max(max_time, t)
            
    # 충돌 횟수 
    result = 0
    for t in range(max_time+1):
        for (x, y), count in d[t].items():
            if count >= 2:
                result += 1
                
    answer = result
    return answer
'''
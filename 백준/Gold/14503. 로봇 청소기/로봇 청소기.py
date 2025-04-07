dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

def out_of_graph(x, y):
    return x<0 or y<0 or x>=N or y>=M

def simulation(graph, N, M, r, c, d):  
    visited = [[False] * M for _ in range(N)]
    visited[r][c] = True

    cnt = 1

    sr, sc, sd = r, c, d

    while True:
        binn = 0

        # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
        for _ in range(4):
            sd = (sd + 3) % 4 # 반시계 방향 90도 회전

            nx = sr + dx[sd]
            ny = sc + dy[sd]

            if out_of_graph(nx, ny) or visited[nx][ny] or graph[nx][ny]==1:
                continue
            else:
                visited[nx][ny] = True
                sr = nx
                sc = ny
                cnt += 1
                binn = 1
                break

        # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
        if binn == 0:
            if (graph[sr - dx[sd]][sc - dy[sd]]==1):
                break
            else:
                sr -= dx[sd]
                sc -= dy[sd]

    return cnt

N, M = map(int, input().split())
r, c, d = map(int, input().split())

graph = []
for _ in range(N):
    row = list(map(int, input().split()))
    graph.append(row)

print(simulation(graph, N, M, r, c, d))
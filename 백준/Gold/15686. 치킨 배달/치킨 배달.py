from collections import deque

N, M = map(int, input().split())
arr = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    row = [0] + list(map(int, input().split()))
    arr[i] = row

homes = []
chickens = []

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if arr[i][j] == 1:
            homes.append((i, j))
        elif arr[i][j] == 2:
            chickens.append((i, j))

# 거리 배열: dists[home_index][chicken_index]
dists = [[0] * len(chickens) for _ in range(len(homes))]
for i, (hx, hy) in enumerate(homes):
    for j, (cx, cy) in enumerate(chickens):
        dists[i][j] = abs(hx - cx) + abs(hy - cy)

min_city_chicken_dist = float('inf')
some_list = list(range(len(chickens)))  # 인덱스 리스트

# 선택된 치킨집 조합(comb)을 가지고 도시 치킨 거리 계산
def do_something(comb: deque):
    global min_city_chicken_dist
    total = 0
    for i in range(len(homes)):
        # 각 집에서 가장 가까운 치킨집까지 거리
        min_dist = min(dists[i][chicken_index] for chicken_index in comb)
        total += min_dist
    min_city_chicken_dist = min(min_city_chicken_dist, total)

# DFS 조합 생성
def dfs(comb: deque, depth: int):
    if len(comb) == M:  # 종료 조건 1
        do_something(comb)
        return
    elif depth == len(some_list):  # 종료 조건 2
        return

    # 현재 depth의 값을 포함한 경우
    comb.append(some_list[depth])
    dfs(comb, depth + 1)

    # 현재 depth의 값을 포함하지 않은 경우
    comb.pop()
    dfs(comb, depth + 1)

dfs(deque(), 0)
print(min_city_chicken_dist)

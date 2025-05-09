N, M = map(int, input().split())

def solution(N, M):
    output = []

    def dfs(start, comb):
        if len(comb) == M:
            output.append(comb[:])
            return 
        
        # 조합 생성 
        for i in range(start, N+1):
            comb.append(i)
            dfs(i+1, comb)
            comb.pop()

    dfs(1, [])

    for comb in output:
        print(" ".join(map(str, comb)))

solution(N, M)

'''
def solution(N, M):
    from itertools import combinations

    for comb in combinations(range(1, N+1), M):
        print(" ".join(map(str, comb)))

solution(N, M) 
''' 
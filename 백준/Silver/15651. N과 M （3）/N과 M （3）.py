N, M = map(int, input().split())

def solution(N, M):
    output = []

    def dfs(comb):
        if len(comb) == M:
            output.append(comb[:])
            return 
        
        # 중복 순열 생성 
        for i in range(1, N+1):           
            comb.append(i)          
            dfs(comb)
            comb.pop()
   
    dfs([])

    for comb in output:
        print(" ".join(map(str, comb)))

solution(N, M)

'''
def solution(N, M):
    from itertools import product

    for comb in product(range(1, N+1), repeat=M):
        print(" ".join(map(str, comb)))

solution(N, M) 
''' 
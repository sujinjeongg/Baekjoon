N = int(input())

def solution(N):
    cnt = [0]
    visited_col = [False] * N 
    visited_d1 = [False] * (2 * N - 1) 
    visited_d2 = [False] * (2 * N - 1) # index 마이너스에 저장이 안 되므로 

    def dfs(row):
        if row == N:
            cnt[0] += 1
            return 

        for col in range(N):
            d1 = row + col
            d2 = row - col 

            if (not visited_col[col]) and (not visited_d1[d1]) and (not visited_d2[d2 + (N-1)]):
                visited_col[col] = True
                visited_d1[d1] = True 
                visited_d2[d2 + (N-1)] = True # index 마이너스에 저장이 안 되므로 
                dfs(row+1)
                visited_col[col] = False 
                visited_d1[d1] = False
                visited_d2[d2 + (N-1)] = False 
            
    dfs(0)
    
    return cnt[0] 

print(solution(N))
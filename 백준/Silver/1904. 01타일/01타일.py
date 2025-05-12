N = int(input())

def solution(N):
    dp = [0 for _ in range(N+2)]
    dp[1] = 1 # 1 추가
    dp[2] = 2 # 00 추가

    for i in range(3, N+1):
        dp[i] = (dp[i-2] + dp[i-1]) % 15746

    print(dp[N])
    '''
    cnt = [0]
    def dfs(length):
        if length == N:
            cnt[0] += 1
            return 
        if length > N:
            return
        
        dfs(length + 1) # 1 추가
        dfs(length + 2) # 00 추가 

    dfs(0)
    
    print(cnt[0]%15746)
    '''

solution(N)
N, K = map(int, input().split())
temperatures = list(map(int, input().split()))

def solution(N, K, temperatures):
    prefix = [0 for _ in range(N+1)]
    for i in range(1, N+1):
        prefix[i] = prefix[i-1] + temperatures[i-1]
        
    dp = [-10**7 for _ in range(N+1)]
    for i in range(K, N+1):
        dp[i] = prefix[i] - prefix[i-K]
        
    print(max(dp))
    
solution(N, K, temperatures)
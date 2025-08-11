N, K = map(int, input().split())

items = []
for _ in range(N):
    W, V = map(int, input().split())
    items.append((W, V))

def solution(N, K):
    dp = [0 for _ in range(K+1)]
    
    for weight, value in items:
        for w in range(K, weight-1, -1):
            dp[w] = max(dp[w - weight] + value, dp[w])
        
    print(dp[K])
    
solution(N, K) 
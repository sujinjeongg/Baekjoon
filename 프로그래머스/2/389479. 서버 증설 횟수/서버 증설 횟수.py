def solution(players, m, k):
    server = [0] * len(players)
    cnt = 0
    
    for i in range(len(players)):
        remain = players[i]-(server[i]*m)
        if remain >= m:
            end = min(i+k, len(players))
            for j in range(i, end):
                server[j] += remain // m
            cnt += remain // m
    return cnt

'''def solution(players, m, k):
    servers = [0 for _ in range(24)] # 증설 서버 수
    cnt = 0 # 증설 횟수 합 
    
    for t in range(24):
        player = players[t] # 이용자 수
        
        remain = player - servers[t]*m # 현재의 서버로 이용자를 할당한 후 할당 받지 못한 이용자 수
        
        if remain > 0:
            plus = (remain+m-1)//m
            start = t
            end = t+k
            if end > 23:
                end = 23
                
            for p in range(start, end):
                servers[p] += plus
            cnt += plus
        
    answer = cnt
    return answer
'''
def solution(players, m, k):
    servers = [0 for _ in range(len(players))] # 증설 서버 수
    cnt = 0 # 증설 횟수 합 
    
    for t in range(len(players)):
        player = players[t] # 이용자 수
        
        remain = player - servers[t]*m # 현재의 서버로 이용자를 할당한 후 할당 받지 못한 이용자 수
        
        if remain >= m:
            plus = remain//m
            start = t
            end = min(t+k, len(players))
                
            for p in range(start, end):
                servers[p] += plus
            cnt += plus
        
    answer = cnt
    return answer
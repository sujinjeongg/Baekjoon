def solution(info, n, m):
    from functools import lru_cache

    length = len(info)
    min_a_sum = [n]  # 리스트로 묶어서 nonlocal 대체

    @lru_cache(maxsize=None)
    def dfs(i, a_sum, b_sum):
        if a_sum >= min_a_sum[0] or b_sum >= m:
            return

        if i == length:
            if a_sum < n and b_sum < m:
                min_a_sum[0] = min(min_a_sum[0], a_sum)
            return

        dfs(i + 1, a_sum + info[i][0], b_sum)  # A에 할당
        dfs(i + 1, a_sum, b_sum + info[i][1])  # B에 할당

    dfs(0, 0, 0)
    return min_a_sum[0] if min_a_sum[0] < n else -1

'''
def solution(info, n, m):      
    idx = []
    
    # [0,0,0], [0,0,1], [0,1,0], ... [1,1,1] 조합 만들기 
    def backtrack(comb):
        if len(comb) == len(info):
            idx.append(tuple(comb))
            return 
        
        for bit in [0,1]:
            comb.append(bit)
            backtrack(comb)
            comb.pop()
            
    backtrack([])
    
    a_sum, b_sum = 0, 0
    min_a_sum = n
    for j in range(len(idx)):
        for k in range(len(info)):
            if idx[j][k] == 0:
                a_sum += info[k][0]
            else:
                b_sum += info[k][1]
                
        if a_sum < n and b_sum < m:
            min_a_sum = min(min_a_sum, a_sum)
        
        a_sum, b_sum = 0, 0
            
    if min_a_sum < n:
        answer = min_a_sum
    else:
        answer = -1

    return answer
'''
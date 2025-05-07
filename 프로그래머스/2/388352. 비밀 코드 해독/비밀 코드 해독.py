def solution(n, q, ans):
    result = [0]  # 결과 개수를 담을 리스트

    def dfs(start, comb):
        # 조합이 5개 완성되었을 때 조건 검사
        if len(comb) == 5:
            for i in range(len(q)):
                cnt = 0
                for num in q[i]:
                    if num in comb:
                        cnt += 1
                if cnt != ans[i]:
                    return  # 하나라도 조건 불일치하면 탈락
            result[0] += 1  # 모든 조건 만족 → 가능한 비밀코드
            return

        # 조합 생성
        for i in range(start, n + 1):
            comb.append(i)
            dfs(i + 1, comb)
            comb.pop()

    dfs(1, [])
    return result[0]

'''def solution(n, q, ans):
    i = [1]
    result = [0]
  
    def dfs(comb):
        if i[0] > n:
            return 
        if len(comb) == 5:
            for j in range(len(q)):
                cnt = 0
                for k in q[j]:
                    if k in comb:
                        cnt += 1
                if cnt != ans[j]:
                    return
            result[0] += 1
      
        i[0] += 1
        comb.append(i[0])
        dfs(comb)
        
        comb.pop()
        dfs(comb)
    
    dfs([])
    
    answer = result[0]
    return answer
'''
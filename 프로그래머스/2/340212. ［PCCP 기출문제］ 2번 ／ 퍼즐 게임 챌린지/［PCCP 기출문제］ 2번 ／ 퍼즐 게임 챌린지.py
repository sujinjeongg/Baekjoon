def solution(diffs, times, limit):
    n = len(diffs)

    def can_clear(level):
        total_time = 0
        for i in range(n):
            if diffs[i] <= level:
                total_time += times[i]
            else:
                mistake_cnt = diffs[i] - level
                prev_time = times[i - 1] if i > 0 else 0
                total_time += (times[i] + prev_time) * mistake_cnt + times[i]
                if total_time > limit:
                    return False
        return total_time <= limit

    left = 1
    right = max(diffs)
    answer = right

    while left <= right:
        mid = (left + right) // 2
        if can_clear(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer

'''def solution(diffs, times, limit):
    from functools import lru_cache
    
    length = len(diffs)
    answer = [float('inf')]
    max_level = 100000  # 종료 조건을 위해 적당히 큰 값 설정
    
    @lru_cache(maxsize=None)
    def dfs(level):
        if level > max_level:
            return 
        
        time = 0
        for i in range(length):
            if diffs[i] <= level:
                time += times[i]
            else:
                time_prev = times[i-1] if i>0 else 0
                time += (times[i] + time_prev)*(diffs[i]-level) + times[i]
        
        if time <= limit:
            answer[0] = level
            return
        else:
            dfs(level+1)
      
    dfs(1)
    answer = answer[0] 
    return answer
'''

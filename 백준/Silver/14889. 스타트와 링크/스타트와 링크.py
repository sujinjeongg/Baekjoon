N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

def solution(N, S):
    from itertools import combinations, permutations

    people = list(range(1, N+1))
    ability_start = 0
    ability_link = 0
    min_diff = float('inf')
    for start in combinations(people, N//2):
        link = tuple(set(people) - set(start)) 
        
        for i in range(N//2):
            for j in range(N//2):
                if i == j:
                    continue
                ability_start += S[start[i]-1][start[j]-1]
                ability_link += S[link[i]-1][link[j]-1]

        min_diff = min(min_diff, abs(ability_start - ability_link))

        ability_start, ability_link = 0, 0

    return min_diff 

print(solution(N, S))
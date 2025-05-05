import sys
input = sys.stdin.readline

N = int(input())

output = []

def solution(N, nums):
    from statistics import mean, median 
    from collections import Counter 

    nums.sort()

    mean = int(round(mean(nums)))
    median = median(nums)

    counter = Counter(nums)
    most_common = counter.most_common()
    most_common_f = most_common[0][1] # 최대 빈도 수
    most_common_v = []
    for v, f in most_common:
        if f == most_common_f and v not in most_common_v:
            most_common_v.append(v)
    if len(most_common_v) > 1:
        mcv = most_common_v[1]
    else:
        mcv = most_common_v[0]

    range = nums[-1] - nums[0]

    output.append(mean)
    output.append(median)
    output.append(mcv)
    output.append(range)
    
nums = [int(input().strip()) for _ in range(N)]

solution(N, nums)
print('\n'.join(map(str, output)))
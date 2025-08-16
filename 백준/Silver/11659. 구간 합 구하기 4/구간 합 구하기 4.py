N, M = map(int, input().split())
nums = list(map(int, input().split()))
ranges = []
for _ in range(M):
    start, end = map(int, input().split())
    ranges.append((start, end))
    
def solution(nums, ranges):
    prefix = [0 for _ in range(N+1)]
    for i in range(1, N+1):
        prefix[i] = prefix[i-1] + nums[i-1]
        
    for start, end in ranges:
        print(prefix[end] - prefix[start-1])
        
solution(nums, ranges)
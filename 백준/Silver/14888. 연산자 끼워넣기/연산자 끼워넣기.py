N = int(input())
nums = list(map(int, input().split()))
plus, minus, multiply, divide = map(int, input().split())

def solution(N, nums, plus, minus, multiply, divide):

    max_v = [-1000000000]
    min_v = [1000000000]
    def dfs(i, plus, minus, multiply, divide, result):
        if i == N:
            max_v[0] = max(max_v[0], result)
            min_v[0] = min(min_v[0], result)
            return
        
        if plus:
            dfs(i+1, plus-1, minus, multiply, divide, result+nums[i])
        if minus:
            dfs(i+1, plus, minus-1, multiply, divide, result-nums[i])
        if multiply:
            dfs(i+1, plus, minus, multiply-1, divide, result*nums[i])
        if divide:
            if result < 0:
                dfs(i+1, plus, minus, multiply, divide-1, -(-result//nums[i]))
            else:
                dfs(i+1, plus, minus, multiply, divide-1, result//nums[i])

    dfs(1, plus, minus, multiply, divide, nums[0])

    print(max_v[0])
    print(min_v[0])

solution(N, nums, plus, minus, multiply, divide)

'''
n_operations = list(map(int, input().split()))

def solution(N, nums, n_operations):
    operations = []

    for i in range(n_operations[0]):
        operations.append('+')
    for i in range(n_operations[1]):
        operations.append('-')
    for i in range(n_operations[2]):
        operations.append('*')
    for i in range(n_operations[3]):
        operations.append('//')

    visited = [False] * (N-1)
    max_v = [-10000000000]
    min_v = [10000000000]
    def dfs(comb):
        if len(comb) == N-1:
            result = nums[0]
            for i in range(1, len(nums)):
                if comb[i-1] == '+':
                    result += nums[i]
                elif comb[i-1] == '-':
                    result -= nums[i]
                elif comb[i-1] == '*':
                    result *= nums[i]
                elif comb[i-1] == '//':
                    result = int(result/nums[i])
            
            max_v[0] = max(max_v[0], result)
            min_v[0] = min(min_v[0], result)
            return 
        
        for i in range(len(operations)):
            if not visited[i]:
                comb.append(operations[i])
                visited[i] = True
                dfs(comb)
                comb.pop()
                visited[i] = False 

    dfs([])

    print(max_v[0])
    print(min_v[0])

solution(N, nums, n_operations)
'''
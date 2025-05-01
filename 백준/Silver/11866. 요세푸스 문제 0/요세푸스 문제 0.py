from collections import deque

N, K = map(int, input().split())

q = deque()

output = [] # 출력값 저장

def solve(N, K):
    for i in range(1, N+1):
        q.append(i)
    
    while N > 1:
        for _ in range(K-1):
            q.append(q.popleft())            
        output.append(q.popleft())

        N -= 1
    output.append(q.pop())

solve(N, K)

print('<' + ', '.join(map(str, output)) + '>')
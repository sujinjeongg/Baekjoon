from collections import deque

q = deque()

def solve(N):
    for i in range(1, N+1):
        q.append(i)

    cnt = N 
    while cnt > 1:
        q.popleft()
        cnt -= 1
        q.append(q.popleft()) # 맨 앞의 원소 꺼내서 뒤에 넣기 

    return q.pop()
        
N = int(input())

print(solve(N))
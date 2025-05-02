from collections import deque

N = int(input())
papers = list(map(int, input().split()))

q = deque()

output = [] # 출력값 저장

def solve(N, papers):
    for i in range(1, N+1):
        q.append((i, papers[i-1]))

    while q:
        ballon, paper = q.popleft()
        output.append(ballon)

        if paper > 0:
            q.rotate(-(paper-1))
        else:
            q.rotate(-paper)

solve(N, papers)
print(' '.join(map(str,output)))
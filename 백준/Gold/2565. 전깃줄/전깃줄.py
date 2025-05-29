N = int(input())
lines = [list(map(int, input().split())) for _ in range(N)]

def solution(N, lines):
    lines.sort(key = lambda x: x[0]) # A 기준 오름차순

    A = [0 for _ in range(N)]
    B = [0 for _ in range(N)]
    for i in range(N):
        A[i], B[i] = lines[i][0], lines[i][1]

    dp = [1 for _ in range(N)]

    for i in range(N):
        for j in range(i):
            if B[i] > B[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(N - max(dp))

solution(N, lines) 
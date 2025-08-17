import sys
input = sys.stdin.readline

S = input().strip()
q = int(input())

questions = []
for _ in range(q):
    a, l, r = input().split()
    questions.append((ord(a)-97, int(l), int(r)))

def solution(S, q):
    prefix = [[0] * (len(S)+1) for _ in range(26)]
    for i in range(1, len(S) + 1):
        for j in range(26):
            prefix[j][i] = prefix[j][i-1]
        prefix[ord(S[i-1]) - 97][i] += 1
        
    for a, l, r in questions:
        print(prefix[a][r+1] - prefix[a][l])

solution(S, q)
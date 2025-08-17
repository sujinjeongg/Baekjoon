S = input()
q = int(input())

questions = []
for _ in range(q):
    a, l, r = input().split()
    questions.append((a, int(l), int(r)))

def solution(S, q):
    for a, l, r in questions:
        print(S[l:r+1].count(a))
        
solution(S, q)        
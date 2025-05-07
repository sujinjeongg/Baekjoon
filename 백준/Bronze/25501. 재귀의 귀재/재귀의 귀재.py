import sys
input = sys.stdin.readline

T = int(input())
S = [input().strip() for _ in range(T)]

def solution(T, S):
    cnt = [0]

    def recursion(s, l, r):
        cnt[0] += 1
        if l>=r: return 1
        elif s[l] != s[r]: return 0
        else: return recursion(s, l+1, r-1)
    
    def isPalindrome(s):
        return recursion(s, 0, len(s)-1)
    
    output = []
    for i in range(T):
        cnt[0] = 0
        output.append((isPalindrome(S[i]), cnt[0]))

    return output 

output = solution(T, S)
for p, cnt in output:
    print(p, cnt)
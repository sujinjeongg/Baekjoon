import sys
input = sys.stdin.readline

N, M = map(int, input().split())

words = [input().strip() for _ in range(N)]

def solution(N, M, words):
    from collections import Counter

    counter = Counter(words)

    filtered = [word for word in counter if len(word)>=M]
    
    output = sorted(filtered, key=lambda word : (-counter[word], -len(word), word))

    return output

output = solution(N, M, words)      
print('\n'.join(output))
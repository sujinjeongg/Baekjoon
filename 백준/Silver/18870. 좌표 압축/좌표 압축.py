N = int(input())

xlist = list(map(int, input().split()))
sorted_x = sorted(set(xlist))
    
rank = {value:idx for idx, value in enumerate(sorted_x)} #idx를 구하는 문제이므로 idx를 value 자리로 옮기기

for x in xlist:
    print(rank[x], end=' ')
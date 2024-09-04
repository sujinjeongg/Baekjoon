N, M = map(int,input().split())

pocketmons = dict()
for i in range(N):
    name = input().strip() #공백으로 인한 오류 예방
    pocketmons[name] = i+1

reverse = {v:k for k,v in pocketmons.items()}
results = []
for _ in range(M):
    search = input().strip()
    if search.isdigit(): # 숫자일 경우 key값을 통해 value값 얻기
        results.append(reverse.get(int(search)))
    else: # 문자일 경우 value값을 통해 key값 얻기
        results.append(pocketmons.get(search))

for result in results:
    print(result)        
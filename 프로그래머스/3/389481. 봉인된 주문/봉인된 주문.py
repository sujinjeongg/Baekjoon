def solution(n, bans):
    def spell2num(spell):
        ans=0
        for ch in spell:
            ans*=26
            ans+=(ord(ch)-ord("a")+1)
        return ans
    def num2spell(num):
        rt=[]
        while num:
            rt.append(num%26 or 26)
            num//=26
            num -= (rt[-1]==26)
        return "".join(map(lambda x:chr(x+ord("a")-1), rt[::-1]))
    b=sorted([spell2num(spell) for spell in bans])
    for od in b:
        if od<=n:
            n+=1
        else:
            break
    return num2spell(n)
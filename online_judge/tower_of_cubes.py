




memo=[]
opposite_sides = {"front":"back","back":"front","left":"right","right":"left","top":"bottom","bottom":"top"}
base_case={"front":0,"back":0,"left":0,"right":0,"top":0,"bottom":0}
counter=0
def all_cases(t,n,s,lvl,memo):
    print(s,lvl)
    if lvl==n:
        print(s,lvl)
        return s
    if len(s)==n:
        print(s,lvl)
        return s
    else:
        s1=s
        s2=s
        for i in t[lvl].keys():
            opp = opposite_sides[i]
            #print(lvl,i)
            if t[lvl][i]==t[lvl-1][s[-1]]:
                s1= all_cases(t,n,s+[opp],lvl+1,memo)
            if len(s1)>=len(s2):
                s2=s1
        if len(s2)>len(s):
            s=s2
        return s



while True:
    largest_stack = []
    counter+=1
    try:
        n=int(input())
        if n==0:
            break
    except EOFError:
        break
    towers = []
    for i in range(n):
        k = [int(x) for x in input().split()]
        p = base_case.copy()
        j=0
        for m in p.keys():
            p[m]=k[j]
            j+=1
        towers.append(p)
    towers=towers[::-1]
    #print(towers)
    print("Case #",counter)
    for i in base_case.keys():
        memo=[i]
        print(all_cases(towers,n,[i],1,memo))
    print()


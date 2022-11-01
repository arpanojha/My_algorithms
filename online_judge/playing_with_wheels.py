
def next_possible_cases(a,forbidden):
    next1=[]
    for i in range(4):
        if a[i]==0:
            p = a[0:i]+[9]+a[i+1:]
            n = a[0:i]+[a[i]+1]+a[i+1:]
        elif a[i]==9:
            p = a[0:i]+[a[i]-1]+a[i+1:]
            n = a[0:i]+[0]+a[i+1:]
        else:
            p = a[0:i]+[a[i]-1]+a[i+1:]
            n = a[0:i]+[a[i]+1]+a[i+1:]
        if p not in forbidden:
            next1.append(p)
        if n not in forbidden:
            next1.append(n)
    return next1

def t1(m,n):
    s=0
    for i in range(4):
        s+=min(abs(m[i]-n[i]),10-max(m[i],n[i])+min(m[i],n[i]))
    return s

def is_closer(a,t,s):
    if t1(a,t)<t1(s,t):
        return True
    else:
        return False

def find_minimum(s,t,c,n,forbidden,visited):
    print(c)
    if c==t:
        print(n)
        return n 
    else:
        k = next_possible_cases(c,forbidden)
        if k==[]:
            return -1
        min_n=n
        all_neg=-1
        for i in k:
            if i in visited:
                continue
            k = find_minimum(s,t,i,n+1,forbidden,visited+[i])
            if k!=-1:
                all_neg=1
            if k!=-1:
                if k<min_n:
                    min_n=k
        if all_neg==-1:
            return -1
        return min_n
                

def kicked_out(d,lvl,s):
    if lvl==4:
        #print(s)
        d[str(s)]=next_possible_cases(s,[])
    else:
        for i in range(10):
            s[lvl]=i
            kicked_out(d,lvl+1,s)

def bfs(n,t,d,forbidden):
    visited=[n]
    fringe=[(n,0)]
    while True:
        if fringe==[]:
            #print(fringe,"broken")
            break
        k= fringe.pop(0)
        if k in forbidden or k in visited:
            continue
        l= d[str(k[0])]
        #print(k,l)
        for i in l:
            if i==t:
                return k[1]+1
            if i not in forbidden:
                #print("forb")
                if i not in visited:
                    #print("vis")
                    visited.append(i)
                    fringe.append((i,k[1]+1))
        #print(fringe)
    return -1


s=[0,0,0,0]
d={}
kicked_out(d,0,s)
# print(len(d))
testcases = int(input())
while testcases>0:
    testcases-=1
    forbidden=[]
    try:
        start=[int(x) for x in input().split()]
        end = [int(x) for x in input().split()]
    except EOFError:
        break
    l = int(input())
    for _ in range(l):
        forbidden.append([int(x) for x in input().split()])
    
    print(start,end,forbidden)
    print(bfs(start,end,d,forbidden))
    # print(next_possible_cases([0,0,0,0],forbidden))
    # print(is_closer([9,0,5,6],[6,5,0,8],[8,0,5,6]))
    # print(find_minimum(start,end,start,0,forbidden,[start]))
    
    


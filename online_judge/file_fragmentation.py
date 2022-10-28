#from functools import cache


def print_two_cases(a,b,n):
    if a+b==n or b+a==n:
        return n
    return None
def list_all_combinations(a,b):
    c = []
    for u in a:
        for w in b:
            c.append(u+w)
            c.append(w+u)
    return c

k = int(input())
m=0
input()
while m<k:
    cache1 = {}
    visited = {}
    m+=1
   
    #print("case ",str(m))
    tot_len=0
    n=0
    l=None
    while l!="":
        try:
            l = input()
            if l=="":
                continue
            #print(l)
            tot_len+=len(l)
            n+=1
            if len(l) not in cache1.keys():
                cache1[len(l)]= []
            cache1[len(l)].append(l)
            visited[l]=None
            #print(cache1)
        except EOFError:
            break
    #print(n)
    """
    if n==2:
        r = []
        for i in cache1.values():
            r.append(i)
        print(r)
        print(r[0])
        print(r[0]+r[1])
        continue
    """
    if tot_len*2%n != 0 or tot_len%2!=0:
        print("no solution")
        print()
        continue 
    h = tot_len*2//n 
    vis = []
    e = 0
    p = []
    good_so_far=[]
    while e<=h:
        perf = []
        if e not in cache1.keys():
            e+=1
            continue
        p = list_all_combinations(cache1[e],cache1[h-e])
        #print(p)
        if p !=[]:
            if good_so_far==[]:
                good_so_far = p
            else:
                for g in p:
                    if g in good_so_far:
                        perf.append(g)
                good_so_far = perf
        #print(p,good_so_far)
        #print()
        e+=1
    print(good_so_far[0])
    print()
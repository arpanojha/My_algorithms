
import math
from textwrap import fill

#k = [226,223,225,224,227,229,228,226,225,227]
#k= [216, 210, 204, 212, 220, 214, 222, 208, 216, 210]
#k = [79950,79936,79942,79962,79954,79972,79960,79968,79924,79932]

def make_combos(a,r,k):
    nums = [a]
    for i in r:
        nums.append(a+i)
    b = []
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            b.append(nums[i]+nums[j])
    b.sort()
    if b==k:
        return True
    return b

def solver(val1,val2,val3,a,r,i,i2=-1,i3=-1):
    if i2==-1:
        r[i] = val1-2*a
    else:
        r[i] = val3-val2
        r[i2] = val3-val1
        a = (val1-r[i])//2
    return a,r

def fill_up(a,r,i,k):
    r[i] = k[0]-2*a
    l = check_combos(a,r,i+1)
    g = k.copy()
    flag=0

    for s in l:

        if s in g:
            g.remove(s)

    return a,r,g,flag

def check_combos(a,r,p):
    nums = [a]
    for i in r[:p]:
        nums.append(a+i)
    b = []
    for i in range(p):
        for j in range(i+1,len(nums)):
            b.append(nums[i]+nums[j])
    b.sort()
    return b
    
while True:
    flag2=0
    try:
        h = input()
    except EOFError:
        break
    k = [int(j) for j in h.split()]
    k=k[1:]
    k.sort()
    a = 0
    n=int(math.sqrt(2*len(k)))+1
    r = [0]*(n-1)
    for i in range(n-1,1,-1):
        a1 = a
        r1=r.copy()
        a1,r1 = solver(k[0],k[1],k[i],a1,r1,0,1)
        for j in range(2,i):
            a1,r1 = solver(k[j],k[0],k[1],a1,r1,j)
        l = check_combos(a1,r1,i)
        g = k.copy()
        flag=0
        for s in l:
            if s not in g:
                flag=1
                break  
            if s in g:
                g.remove(s)
        if flag==1:
            continue
        for w in range(i,len(r1)):
            a1,r1,g,flag = fill_up(a1,r1,w,g)
        
        if g==[]:
            flag2=1
            e = str(a1)
            for q in range(len(r1)):
                e+=" "+str(a1+r1[q])
            print(e)
            break

    if flag2==0:
        print("Impossible")

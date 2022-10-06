

def sum_frac(now,prev):
    k = []
    k.append((now[0][0]+prev[0][0],now[0][1]+prev[0][1]))
    k.append((now[0][0]+prev[1][0],now[0][1]+prev[1][1]))
    return k
def check_L_R(cur,c,a):
    L = cur[0]
    R = cur[1]
    a=a[0]
    if L==a:
        return 'L'
    elif R==a:
        return 'R'
    c=c[0]
    if a[0]*c[1]<a[1]*c[0]:
        return 'L'
    elif a[0]*c[1]>a[1]*c[0]:
        return 'R'
    else:
        return ''
while True:
    prev = [(0,1),(1,0)]
    now = [(1,1)]
    try:
        k = input()
        m = [int(i) for i in k.split()]
    except EOFError:
        break
    x,y = m[0],m[1]
    s = ''
    curr = now
    m=0
    if x==1 and y==1:
        break
    while True:
        m+=1
        curr_1 = sum_frac(curr,prev)
        if curr ==[(x,y)]:
            break
        dir = check_L_R(curr_1,curr,[(x,y)])
        s+=dir
        if dir=='L':
            prev[1]=curr[0]
            curr = [curr_1[0]]
            
        else:
            prev[0]=curr[0]
            curr=[curr_1[1]]
    print(s)

# This code gives runtime errors on uva but runs locally. 


def strip_scientists(paper):
    i=0
    j=0
    p2 = paper.split(":") 
    p = p2[0].split(",")
    print(p)
    p1=[]
    for i in range(0,len(p),2):
        if " " == p[i][0]:
            p[i] = p[i][1:]
        if " "==p[i+1][-1]:
            p[i+1]= p[i+1][:-1]
        p1.append(p[i]+","+p[i+1])
    return p1

def create_map(dict_sci,sci_list):
    for i in dict_sci:
        if i not in sci_list:
            sci_list[i]=set([])
        
        for j in dict_sci:
            if j not in sci_list[i] and j!=i:
                sci_list[i].add(j)
    return sci_list

def shortest_path(graph,min_path):
    visited= []
    next_sci = ['Erdos, P.']
    min_path[next_sci[0]]=0
    while len(next_sci)!=0:
        i = next_sci.pop(0)
        visited.append(i)
        for k in graph[i]:
            if k not in visited:
                if min_path[k]==-1:
                    min_path[k]=min_path[i]+1
                min_path[k] = min(min_path[i]+1,min_path[k])
                next_sci.append(k)
    return min_path


scenario = int(input())
scene = 0
while scene<scenario:
    scene+=1
    PN = input().split()
    P,N = int(PN[0]),int(PN[1])
    i = 0
    j=0
    papers= []
    op_sci = []
    while i<P:
        i+=1
        papers.append(input())
    sci_list = {}
    while j<N:
        j+=1
        op_sci.append(input())
    if P==0:
        for j in op_sci:
            print("{} infinity".format(j))
        break
    for i in papers:
        sci_list = create_map(strip_scientists(i),sci_list)
    distances = {}
    for i in sci_list.keys():
        distances[i] = -1#sys.maxsize
    distances = shortest_path(sci_list,distances)
    print("Scenario {}".format(scene))
    for j in op_sci:
        if distances[j]==-1:#sys.maxsize:
            print("{} infinity".format(j))
        else:
            print("{} {}".format(j,distances[j]))
   
        

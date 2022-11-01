



def check_colouring(g,i,colour,available_colour,visited):
    if i==len(colour):
        return 1
    else:
        next_colour=""
        if available_colour==allowed_colours[0]:
            next_colour=allowed_colours[1]
        else:
            next_colour=allowed_colours[0]
        for m in g[i]:
            if colour[m]!="" and colour[m]!=available_colour:
                return 0
            colour[m]=available_colour
            if m in visited:
                continue
            k = check_colouring(g,m,colour,next_colour,visited+[m])
            if k==0:
                return 0
        return 1
            

allowed_colours=['a','b']
counter=0
while True:
    counter+=1
    colour = {}
    try:
        n = int(input())
        if n==0:
            break
    except EOFError:
        break
    l = int(input())
    graph={}
    for i in range(n):
        colour[i]=""
    for _ in range(l):
        g = [int(x) for x in input().split()]
        if g[0] not in graph.keys():
            graph[g[0]]=[]
        if g[1] not in graph.keys():
            graph[g[1]]=[]
        graph[g[0]].append(g[1])
        graph[g[1]].append(g[0])

    # if counter==11:
    #     print(graph,colour)

    colour[0]='a'
    p = ['NOT BICOLORABLE.','BICOLORABLE.']
    if n==1:
        print(p[1])
        continue
    print(p[check_colouring(graph,0,colour,'b',[0])])
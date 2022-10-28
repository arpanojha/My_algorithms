
# Geenerate a graph of nearest neighbours and then hamiltonian path

def all_subsets(n,level=0,vis=[],s=[]):
	s.sort()
	#print(s)
	if s not in vis:
		vis.append(s)
	if level>=n:
		#print(s)
		return
	else:
		for i in range(n):
			#s.append(i)
			if i in s:
				continue
			k=s+[i]
			k.sort()
			if k in visited:
				continue
			all_subsets(n,level+1,vis,s+[i])


def next_possible(n,s,visited):
	next_ = []
	if len(s)<n+1:
		for i in range(n):
			g = s+[i]
			g.sort()
			#print("s+i ",g,visited)
			if i in s:
				continue
			elif g in visited:
				continue
			else:
				next_.append(g)
	for i in range(len(s)):
		k = s[:i]+s[i+1:]
		#print("k ",k)
		if k in visited:
			continue
		else:
			next_.append(k)
		#print("next ",next_)
	return next_


def generate_list_of_strings(m):
	k=[]
	for i in m:
		k.append(generate_strings(i))
	return k
def generate_strings(a=[]):
	if a==[]:
		return " "
	else:
		return " ".join([str(i) for i in a])



testcases =  int(input())
while testcases>=0:
	graph={}
	testcases-=1
	try:
		n,k=[int(x) for x in input().split()]
		a = [int(x) for x in input().split()]
	except EOFError:
		break
	i=0
	a.sort()
	#n=10
	s = [-1 for _ in range(n)]
	visited=[]
	all_subsets(n,0,visited)
	#print(visited)
	for i in visited:
		graph[generate_strings(i)] = generate_list_of_strings(next_possible(n,i,[]))
	start=generate_strings(a)
	vis = [start]
	next_1 = graph[start]
	while next_1!=[]:
		if len(vis)==2**n:
			#print(len(vis))
			#print(vis)
			for i in range(2**n):
				print(str(i)+": "+vis[i])
			break
		k = next_1.pop(0)
		if k in vis:
			continue
		vis.append(k)
		n_1 = graph[k]
		next_1 = n_1+next_1
	print()


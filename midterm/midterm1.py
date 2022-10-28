# All subsets and dynamic programming . 


def subsets_1(a,t,n=0,s=0,memo={}):
	if s>=t:
		return s,n
	else:
		if len(a)==0:
			return 10000000000,102
		s1,n1 = subsets_1(a[1:],t,n+1,s+a[0],memo)
		s2,n2 = subsets_1(a[1:],t,n,s,memo)
		if s1<s2:
			if s1 not in memo.keys():
				memo[s1]=n1
			else:
				memo[s1]=min(n1,memo[s1])
			return s1,n1
		else:
			if s1 not in memo.keys():
				memo[s1]=n1
			else:
				memo[s1]=min(n1,memo[s1])
			return s2,n2
	



testcases=int(input())
while testcases>=0:
	memo={}	
	a=[]
	try:
		t = int(input())
		n = int(input())
		for i in range(n):
			a.append(int(input()))
	except EOFError:
		break
	op = subsets_1(a,t,0,0,memo)
	min_n=[0]
	min_s=[0]
	print(str(op[0])+" "+str(memo[op[0]]))
	testcases-=1

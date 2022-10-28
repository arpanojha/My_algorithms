# permulations problem 

d = {'A':1,
	 'B':2,
	 'C':3,
	 'D':4,
	 'E':5,
	 'F':6,
	 'G':7,
	 'H':8,
	 'I':9,
	 'J':10,
	 'K':11,
	 'L':12,
	 'M':13,
	 'N':14,
	 'O':15,
	 'P':16,
	 'Q':17,
	 'R':18,
	 'S':19,
	 'T':20,
	 'U':21,
	 'V':22,
	 'W':23,
	 'X':24,
	 'Y':25,
	 'Z':26}


def C(n,r):
	v = n-r+1
	a = 1
	for i in range(v,n+1):
		a*=i
	return a
def answer(v):
	visited=[]
	n=len(v)
	an = 0

	for i in range(n):
		k = d[v[i]]-1
		if visited==[]:
			l = k*C(26-i-1,n-1-i)
		else:
			for j in visited:
				if d[j]<d[v[i]]:
					k-=1
			l = k*C(26-i-1,n-1-i)
		an+=l
		visited.append(v[i])
	print(an)


n = int(input())
while n>=0:
	n-=1
	try:
		a = input().strip()
	except EOFError:
		break
	answer(a)



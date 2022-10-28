# L(k,d) is the number of labelling k-RY TREE 
# N is number of nodes
# N(2,d) = 2^(d+1)-1
# N(k,d) = (k^(d+1)-1)/(k-1)
#

# L(k,d) = (n-1)Cd * k^(d-1)

#(N(k,d) - 1) C N(k,d)-1/k)((n-i - (x-1)/k)) 
# 
#x =  (N(k,d)-1)/k
# (N(k,d)-1 C x)(N(k,d)-1-xC x)... (X C X)
# P = (N(k,d) -1)!/(N(k,d)-1)/k !)^k

# L = (L(k,d-1)^k) * P
# L(k,0)=1
import operator as op
from functools import reduce

memo={}
for i in range(22):
	memo[str(i)+" 0"] = 1


#print(memo)
def N(k,d):
	if k==1:
		return 0
	return (k**(d+1)-1)//(k-1)

def P(k,d):
	p = 1
	n = N(k,d)-1
	x = n//k
	while n-x!=0:
		p*=C(n,x)
		n-=x
	return p

def C(n,x):
	x = min(x,n-x)
	num = reduce(op.mul, range(n,n-x,-1),1)
	den = reduce(op.mul, range(1,x+1),1)
	return num//den

def L(k,d):
	if d==0:
		return 1
	else:
		b = P(k,d)*(L(k,d-1)**k)
		return b

#print(L(10,1))
while True:
	try:
		h = input().split()
		a,b = int(h[0]),int(h[1])
	except EOFError:
		break
	print(L(a,b))
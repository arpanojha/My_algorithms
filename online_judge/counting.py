s = {1:2,2:5,3:13}

# C_n = 2*C_n-1 +C_n-2 + C_n-3
def rec_rel(n):
	if n in s.keys():
		return s[n]
	else:
		C1 = 2*rec_rel(n-1) + rec_rel(n-2)+ rec_rel(n-3)
		s[n]=C1
		return C1
while True:
	try:
		n=int(input())
	except EOFError:
		break

	print(rec_rel(n))


def slowest_two(island):
	max_arr=max(island)
	cpy = island[:]
	cpy.remove(max_arr)
	next_max = max(cpy)
	return max_arr,next_max

def algorithm_1(island_1,op):
	a = str(island_1[0])
	x = str(island_1[-1])
	y = str(island_1[-2])
	if island_1!=[]:
		op+=a+" "+y+"\n"+a+"\n"+a+" "+x+"\n"+a+"\n"
	return op

def algorithm_2(island_1,op):
	a = str(island_1[0])
	b = str(island_1[1])
	x = str(island_1[-1])
	y = str(island_1[-2])
	if island_1!=[]:
		op+=a+" "+b+"\n"+a+"\n"+y+" "+x+"\n"+b+"\n"
	return op

k = int(input())

while k>0:
	input()
	k-=1
	island_1 = []
	length = int(input())
	while length>0:
		island_1.append(int(input()))
		length-=1

	time_taken=0
	island_1.sort()
	op = ""
	while island_1!=[]:
		a = island_1[0]
		if len(island_1)==1:
			op+=str(a)+"\n"
			time_taken+=a 
			break
		b = island_1[1]
		if len(island_1)==2:
			op+=str(a)+" "+str(b)+"\n"
			time_taken+=b
			break
		if len(island_1)==3:
			op+=str(a)+" "+str(b)+"\n"+str(a)+"\n"+str(a)+" "+str(island_1[-1])+"\n"
			time_taken+=sum(island_1)
			break
		x,y = slowest_two(island_1)
		if 2*b>a+y:
			op = algorithm_1(island_1,op)
			time_taken+= 2*a+x+y
		else:
			op = algorithm_2(island_1,op)
			time_taken+=2*b+a+x
		island_1.remove(x)
		island_1.remove(y)
		island_1.sort()
	print(time_taken)
	print(op)
#print()
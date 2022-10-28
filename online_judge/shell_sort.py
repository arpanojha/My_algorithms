k = int(input())
while k>=1:
	k-=1
	h = int(input())
	actual_lot = []
	desired_lot = {}
	for i in range(h):
		actual_lot.append(input())
	for i in range(h):
		desired_lot[input()] = i
	#print(actual_lot)
	#print(desired_lot)
	l=-1
	f=-1
	for i in range(len(actual_lot)):
		if desired_lot[actual_lot[i]]<l and desired_lot[actual_lot[i]]>f:
			f=desired_lot[actual_lot[i]]
		if desired_lot[actual_lot[i]]>l:
			l=desired_lot[actual_lot[i]]
	#print(f)
	op_lst=list(desired_lot.keys())
	if f!=-1:
		for i in range(f,-1,-1):
			print(op_lst[i])
	print()




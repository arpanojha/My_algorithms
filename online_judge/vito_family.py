

def avg(num_cases,streets):
	if num_cases%2:
		return streets[num_cases//2]
	else:
		return (streets[num_cases//2-1]+streets[num_cases//2])/2

k = int(input())
while k>=1:
	distances=0
	try:
		p = [int(x) for x in input().split()]
		#print(p)
	except EOFError:
		break
	num_cases,streets = p[0],p[1:]
	streets.sort()

	if num_cases==0:
		print(0)
		continue
	l = avg(num_cases,streets)
	for j in streets:
		distances+=abs(j-l)
	print(int(distances))
	k-=1

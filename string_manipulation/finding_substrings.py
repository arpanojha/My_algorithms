m=[]
a="asdfghjkl"
b="asdf"
def main():
	substr(b)

def substr(a,i=0,j=-100):
	if j == -100:
		j=len(a)
	if i+1>=j:
		return a
	substr(a,i,j-1)
	substr(a,i+1,j)
	for n in range(i,j):
		print(a[n],end = " ")
	print()


if __name__ == '__main__':
	main()

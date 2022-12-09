class polygon:
	def __init__(self,a=[]):
		self.points = a
		self.area = 0
	def get_area(self):
		l = len(self.points)
		self.area=0
		for i in range(1,l):
			a = self.points[i-1]
			b = self.points[i]
			self.area+=a[0]*b[1]-a[1]*b[0]
		self.area+=self.points[-1][0]*self.points[0][1]-self.points[-1][1]*self.points[0][0]
		self.area/=2
s = polygon()
while True:
	try:
		s.points.append([float(x) for x in input().split()])
	except EOFError:
		break

s.get_area()
print(s.area)

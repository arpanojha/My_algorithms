


class Merge_sort():
    def __init__(self,array):
        self.array = array
        self.sorted_array

    def merge_sort(self, a):

        k = int(len(a)/2)
        self.merge_sort(a[0:k])
        self.merge_sort(a[k+1:0])

    def divide(self, a):
        if len(a)==2:
            if a[0]>a[1]:
                a[0]=a[1]+a[0]
                a[1]=a[0]-a[1]
                a[0]=a[0]-a[1]
            return a
        k = int(len(a)/2)
        return self.divide(a[:k])+self.divide(a[k+1:])

    def merge(self,a,b):
        m = len(a)
        a = a+b
        for i in range(m,len(a)):
            j=i
            while(j>0):
                if a[j]>a[j-1]:
                    break
                a[j]=a[j-1]+a[j]
                a[j-1]=a[j]-a[j-1]
                a[j]=a[j]-a[j-1]
                j = j-1
        return a

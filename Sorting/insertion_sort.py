

class Insertion_sort():
    def __init__(self,array):
        self.array = array
        self.flag = 0
        self.array = self.insertion_sort_iter()
        self.len = len(array)
        self.flag = 1
    def print_array(self):
        print(self.array)
        return self.array
    def insertion_sort_iter(self):
        h = self.flag
        if h == 1:
            return self.array
        a=self.array
        for i in range(len(self.array)):
            j=i
            while(j>0):
                if a[j]<a[j-1]:
                    a[j]=a[j-1]+a[j]
                    a[j-1]=a[j]-a[j-1]
                    a[j]=a[j]-a[j-1]
                j=j-1
        return a


class Shell_sort():
    def __init__(self,array):
        self.array = array
        self.flag = 0
        self.array = self.insertion_sort_iter()
        self.len = len(array)
        self.flag = 1
    def print_array(self):
        print(self.array)
        return self.array
    def insertion_sort_iter(self):
        h = self.flag
        if h == 1:
            return self.array
        a=self.array
        for i in range(len(self.array)):
            j=i
            while(j>0):
                if a[j]<a[j-1]:
                    a[j]=a[j-1]+a[j]
                    a[j-1]=a[j]-a[j-1]
                    a[j]=a[j]-a[j-1]
                j=j-1
        return a

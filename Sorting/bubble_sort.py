

class Bubble_sort():
    def __init__(self,array):
        self.array = array
        self.array = self.bubble_sort_iter()
        self.len = len(array)
    def print_array(self):
        print(self.array)
        return self.array
    def bubble_sort_iter(self):
        a=self.array
        for i in range(len(self.array)):
            flag = 0
            for j in range(len(self.array)-1):
                if a[j]>a[j+1]:
                    a[j]=a[j+1]+a[j]
                    a[j+1]=a[j]-a[j+1]
                    a[j]=a[j]-a[j+1]
                    flag = flag+1
            if flag == 0:
                break
        return a

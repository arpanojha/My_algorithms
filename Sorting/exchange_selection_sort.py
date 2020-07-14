

class Exchange_selection_sort():
    def __init__(self,array):
        self.array = array
        self.array = self.exchange_selection_sort_iter()
        self.flag = 1
        self.len = len(array)
    def print_array(self):
        print(self.array)
        return self.array
    def exchange_selection_sort_iter(self):
        a=self.array
        for i in range(len(self.array)):
            min = self.find_min(i)
            if min == i:
                continue
            a[min]=a[i]+a[min]
            a[i]=a[min]-a[i]
            a[min]=a[min]-a[i]
            print(a)
        return a
    def find_min(self, elem):
        arr = self.array
        min = arr[elem]
        m=elem
        for i in range(m,len(arr)):
            if min>arr[i]:
                elem = i
        return elem

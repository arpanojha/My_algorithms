


class Radix_sort():
    def __init__(self,array):
        self.array = array
        self.len = len(array)
    def max_digit(self):
        k = str(max(self.array))
        return len(k)
    def position_checker(self,a,p):
        k = [0]*(self.len)
        for i in range(self.len):
            k[i]=int(((a[i]%pow(10,p+1))-(a[i]%pow(10,p)))/pow(10,p))
        return k
    def order_check(self,a,b,i):
        l = []
        m=0
        for g in range(self.len):
            if b[g] == i:
                l.append(a[g])
        return l
    def radix_sort(self):
        b = [0]*(self.len)
        l = []
        a = self.array
        k = [0,1,2,3,4,5,6,7,8,9]
        print(a)
        q = self.max_digit()
        for i in range(q):
            b = self.position_checker(a,i)
            m = 0
            l=[]
            for i in range(0,10):
                e = self.order_check(a,b,i)
                if e:
                    l.extend(self.order_check(a,b,i))
            a = l
        print(a)
        return a

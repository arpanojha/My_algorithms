h = 0.05
x0 = 0.0
y0 = 1.0
x = 2.0
n = int((x-x0)/h)

def main():
    #print("n: ",n)

    print(iterate_tofind(x0,y0,h))



def differential(x,y):
    f = (x-y)/2
    return f
def find_rk(x,y,h):
    k1 = h*differential(x,y)
    k2 = h*differential(x+(h/2),y+(k1/2))
    k3 = h*differential(x+(h/2),y+(k2/2))
    k4 = h*differential(x+h,y+k3)
    y1 = y + (k1/6) + (k2/3) + (k3/3) + (k4/6)
    return y1

def iterate_tofind(x,y,h):
    for i in range(0,n):
        y1 = find_rk(x,y,h)
        y = y1
        x= x+h
    return y

if __name__ == '__main__':
    main()

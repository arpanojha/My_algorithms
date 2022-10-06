

def get_table(k):
    p = {}
     

while True:
    try:
        k = int(input())
    except EOFError:
        break
    #p = get_table(k)
    s = '11'
    p = 0
    while int(s)%k!=0:
        s+='1'
    print(len(s))

def counting_sort(A,B,k):
    C=[0]*k
    for j in range(len(A)):
        C[A[j]]+=1
    for i in range(1,k):
        C[i]=C[i]+C[i-1]
    j=0
    for j in range(len(A)-1,-1,-1):
        B[C[A[j]]-1]=A[j]
        C[A[j]]-=1
    #print(C)
    return B
    
#A=[3,2,3,0]
A=[5,1,3,0,4,2,6,3,1,2]
B=[0]*len(A)
print(counting_sort(A,B,max(A)+1))

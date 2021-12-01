def bin_search(A,n,i,j):  # A is the search array, n is the string/number to be searched, i,j is the positions between the array to be searched
    if j<=i:
        if A[i]==n:
            return True
        return False
    mid=A[i+(j-i)//2]
    #print(mid,i,j,n)
    if mid <= n:
        if mid == n:
            return True
        return bin_search(A,n,i+((j-i)//2)+1,j)
    elif mid >= n:
        if mid ==n:
            return True
        return bin_search(A,n,i,i+((j-i)//2)-1)
   

# think caterpillar. Tha largest of the array so far is compared to current element for that largest contiguoous subarray
# pass an array and it solves the largest subsequence sum in O(N) time.
def caterpillar(n):
        root  = n[0]
        tail = n[0]
        for i in range(1,len(n)):
            tail+=n[i]
            tail = max(tail,n[i])
            root = max(root,tail)
        return root

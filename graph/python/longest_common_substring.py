#LCS Q4 this may not work on jupyter with external files we have run it on linux server and pasted results below
import sys


def lcs_back(C,A,B,i,j,seq=""):
    #print(i,j,A[i],B[j])
    if i==0 or j==0:
        return seq
    if A[i] == B[j]:
        #print(A[i],B[j],i,j)
        seq=A[i]+seq
        return lcs_back(C,A,B,i-1,j-1,seq)
    if C[i][j-1] > C[i-1][j]:
        return lcs_back(C,A,B,i,j-1,seq)
    return lcs_back(C,A,B,i-1,j,seq)

def lcs_back_iter(C,A,B):
    seq=""
    i=len(A)-1
    j=len(B)-1
    while i>=0 and j>=0:
        if A[i]==B[j]:
            seq=A[i]+seq
            i-=1
            j-=1
        if C[i][j-1] > C[i-1][j]:
            j-=1
        else:
            i-=1
    return seq


def lcs(A,B):
    n,m=len(A),len(B)
    A=" "+A
    B=" "+B
    c=[[0 for x in range(m+1)] for x in range (n+1)]
    seq=""
    #print(len(c),len(c[0]))
    for i in range(1,n+1):
        equated=0
        for j in range(1,m+1):
            #print(i,j)
            if A[i]==B[j]:
                c[i][j]=c[i-1][j-1]+1
                #print(i,j,A[i],B[j])
                equated=1
            else:
                c[i][j]=max(c[i-1][j],c[i][j-1])
        if equated==1:
            seq+=A[i]
    return c


def open_file(f_name):
    lin=[]
    enc='utf-8'
    with open(f_name,encoding=enc) as f:
        lin=f.readlines()

    data=""
    for l in lin:
        data+=str(l)
    print(len(data))
    return data

def brute_force_1(T,P):
    n,m=len(T),len(P)
    pat1=""
    pat2=""
    j=0
    for i in range(n):
        #print(i,j)
        if j==m:
            break
        if T[i]==P[j]:
            j+=1
            pat1+=T[i]
    i=0
    for j in range(n):
        if i==n:
            break
        if T[i]==P[j]:
            i+=1
            pat2+=P[j]
    if len(pat1)>len(pat2):
        return pat1
    else:
        return pat2

def brute_force(T,P):
    count_lcs=0
    max_lcs=0
    seq=""
    lcs=""
    n,m =len(T),len(P)
    for i in range(n-m):
        for j in range(m):
            h=j
            count_lcs=0
            seq=""
            for k in range(i+j,i+m):
                if T[k]==P[h]:
                    count_lcs+=1
                    seq+=T[k]
                    h+=1
               #     print(seq)
                else:
                    break
            if max_lcs<count_lcs:
                print(seq)
                max_lcs=count_lcs
                lcs=seq
    return lcs


def main():

    #file1="C:\Users\New User\human_tp53.txt"
    #file2="C:\Users\New User\sheep_mef2b.txt"
       # seq1=open_file(file1)
       # seq2=open_file(file2)
       # seq1=seq1
       # seq2=seq2
    seq1="XMJYAUZ"
    seq2="MZJAWXU"
    seq1="AGCAT"
    seq2="GAC"
    return lcs_back_iter(lcs(seq1,seq2)," "+seq1," "+seq2)
   

print(main())


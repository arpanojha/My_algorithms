import numpy as np
import scipy
from scipy import stats
import math
import random
import re

def function(X,mu,sig):
    return stats.multivariate_normal.pdf(X,mu,sig)  # gaussian distribution

def abs_diff(a,b):
    return (a - b)**2

def diff(mu,mu_new):
    get_diff = np.vectorize(abs_diff)
    give_me_diff_matrix = get_diff(mu,mu_new)
    sum_of_diff = sum(sum(give_me_diff_matrix))
    return sum_of_diff

def re_estimate_priors(w):
    return sum(w)

def re_estimate_mean(w,D):
    sum_w = sum(w)
    return np.matmul(w,D)
def transpose(a):
    return np.matrix.transpose(a)
def x_mu_difference(x,mu):
    return x-mu
def multiply_matrices(a,b):
    return np.matmul(a,b)
def re_estimate_covariance(w,D,mu,size):
    sum_w=sum(w)
    diff_x_mu = np.vectorize(x_mu_difference)
    k=np.identity(size)/1000
    for j in range(len(w)):
        x_mu = diff_x_mu(D[j],mu)
        l=multiply_matrices(x_mu,transpose(x_mu))
        t=np.matrix(x_mu).T
        x_mu = np.matrix(x_mu)
        l=multiply_matrices(t,x_mu)
        k = np.add(k,w[j]*l)
    return k/sum_w
#np.random.seed(23)
#random.seed(23)
def e_m(D,k,e):
    t=0
    n = len(D)   #351
    d = len(D[0])   #34
    mu = np.random.rand(k,d)           # k*d
    sigma = [np.identity(d) for _ in range(k)]   # d*d * k
    p = [1/k for _ in range(k)]   # 1 * k
    p = np.array(p)
    mu_new = [[ 0 for _ in range(d)] for _ in range(k)]  # k*d
    w = np.zeros((k,n))
    while diff(mu,mu_new) > e:
        if t!=0:
            mu = mu_new.copy()
        for i in range(k):
            for j in range(n):
                h= function(np.matrix(D[j]),mu[i],sigma[i])
                w[i][j] = h * p[i]
        w_sums_column=w.sum(axis=0)
        for i in range(n):
            for j in range(k):
                w[j][i]=w[j][i]/w_sums_column[i]
        w_sums = w.sum(axis=1)
        for i in range(k):
            mu_new[i] = re_estimate_mean(w[i],D)/w_sums[i]
            sigma[i] = re_estimate_covariance(w[i],D,mu[i],d)
            p[i] = w_sums[i] / n
       # print("iteration {} {}".format(t,sum(p)))
    #    print("mu = ", mu)
    #    print("mu_new =", mu_new)
     #   print("p = ", p)
   #     print("w = ",w)
   #     print("sigma = ",sigma)
    #    print("diff =",diff(mu,mu_new))
        t+=1
   # print("mean values = ",mu)
   # print("Number of iterations : ",t)
    return mu,t-1


D=[]
h=[]
k=3
e=0.000001
mu=[0.4,0.1,0.02,0.9,0.7]
sigma=[1,1.2,0.4,0.5,0.1]
for i in range(5):
    s = np.random.normal(mu[i], sigma[i], 500)
    h.append(s)
D=np.matrix(h).T
D=D.tolist()
#print(D.shape)
print(D[1])
print(e_m(D,k,e))


import numpy as np
from pylab import *
from math import *
import mpl_toolkits.mplot3d

global error
error=1e-5

def Jacobi(L):
    V0=[[0 for i in range(L)]for j in range(L)]#i represents x, j represents y
    a=int(2*(L-1)/5)
    b=int(3*(L-1)/5)
    for i in [a]:
        for j in range(a,b+1):
            V0[j][i]=1.0# j,i

    for i in [b]:
        for j in range(a,b+1):
            V0[j][i]=-1.0

    VV=[]
    VV.append(V0)
    s=0
    dx=0.1
    #iteration
    while 1:
        VV.append(V0)
        for i in range(1,L-1):
            for j in range(1,L-1):
                VV[s+1][i][j]=(VV[s][i+1][j]+VV[s][i-1][j]+VV[s][i][j+1]+VV[s][i][j-1])/4.0
        for i in [a]:
            for j in range(a,b+1):
                VV[s+1][j][i]=1.0
        for i in [b]:
            for j in range(a,b+1):
                VV[s+1][j][i]=-1.0
        VV[s]=np.array(VV[s])
        VV[s+1]=np.array(VV[s+1])
        dVV=VV[s+1]-VV[s]
        dV=0
        for i in range(1,L-1):
            for j in range(1,L-1):
                dV=dV+abs(dVV[i][j])

        s=s+1
        print dV
        if dV<error*(L-1)**2 and s>10:
        #if dV<error and s>10:
            break
    return s

def GS(L):
    V0=[[0 for i in range(L)]for j in range(L)]#i represents x, j represents y
    a=int(2*(L-1)/5)
    b=int(3*(L-1)/5)
    for i in [a]:
        for j in range(a,b+1):
            V0[j][i]=1.0# j,i

    for i in [b]:
        for j in range(a,b+1):
            V0[j][i]=-1.0

    VV=[]
    VV.append(V0)
    s=0
    dx=0.1
    #iteration
    while 1:
        VV.append(V0)
        for i in range(1,L-1):
            for j in range(1,L-1):
                VV[s+1][i][j]=(VV[s][i+1][j]+VV[s+1][i-1][j]+VV[s][i][j+1]+VV[s+1][i][j-1])/4.0
        for i in [a]:
            for j in range(a,b+1):
                VV[s+1][j][i]=1.0
        for i in [b]:
            for j in range(a,b+1):
                VV[s+1][j][i]=-1.0
        VV[s]=np.array(VV[s])
        VV[s+1]=np.array(VV[s+1])
        dVV=VV[s+1]-VV[s]
        dV=0
        for i in range(1,L-1):
            for j in range(1,L-1):
                dV=dV+abs(dVV[i][j])
        s=s+1
        if dV<error*(L-1)**2 and s>10:
        #if dV<error and s>10:
            break
    return s

def SOR(L):
    a=int(2*(L-1)/5)
    b=int(3*(L-1)/5)
    V0=[[0 for i in range(L)]for j in range(L)]#i represents x, j represents y

    for i in [a]:
        for j in range(a,b+1):
            V0[j][i]=1.0# j,i

    for i in [b]:
        for j in range(a,b+1):
            V0[j][i]=-1.0
    VV=[]
    VV.append(V0)
    alpha=2.0/(1+pi/L)
    s=0
    dx=0.1
#iteration
    while 1:
        VV.append(V0)
        for i in range(1,L-1):
            for j in range(1,L-1):
                VV[s+1][i][j]=(VV[s][i+1][j]+VV[s+1][i-1][j]+VV[s][i][j+1]+VV[s+1][i][j-1])/4.0
        for i in [a]:
            for j in range(a,b+1):
                VV[s+1][j][i]=1.0
        for i in [b]:
            for j in range(a,b+1):
                VV[s+1][j][i]=-1.0
        VV[s]=np.array(VV[s])
        VV[s+1]=np.array(VV[s+1])
        dVV=VV[s+1]-VV[s]
        VV[s+1]=alpha*dVV+VV[s]
        dV=0
        for i in range(1,L-1):
            for j in range(1,L-1):
                dV=dV+abs(alpha*dVV[i][j])
        print dV,L 
          
        s=s+1
        if dV<error*(L-1)**2 and s>10:
        #if dV<error and s>10:
            break
    return s
f=open('problem5.7.txt','w')
print >> f,'L','J','GS'
for i in range(6,51,5):
    print >> f,i,Jacobi(i),GS(i)
print >> f,'L','SOR'
for i in range(6,30,2):#without 31
    print >> f,i,SOR(i)
f.close()
print 'end'

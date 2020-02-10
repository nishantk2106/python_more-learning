from array import *
def binaryarraysort():
    n=int(input("Enter the size of array"))
    ar=array('i',[])
    k=0
    for i in range(n):
        p=int(input("Enter the binary number"))
        if (p==0 or p==1):
            ar.append(p)
        else:print("Enter the valid number either 0 or 1")

    for c in range(0,n):
        if (ar[c]==0):
            ar[k]=0
            print(ar[k])
            k=k+1
    for p in range(k,n):
        ar[p]=1
        print(ar[p])
binaryarraysort()


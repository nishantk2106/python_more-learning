# given an aaray find the sum 0 is present or not in array
#input={3,4,-7,3,1,3,1,-4,-2,-2}

from array import *
def sumarray():
    sum=0
    n=int(input("Enter the length of array"))
    arr=array('i',[])
    for i in range(n):
        c=int(input("Enter the value in array :"))
        arr.append(c)
    for p in range(n):
        sum=0
        for q in range(p,n):
            sum=sum+arr[q]
            if(sum==0):
                print("Subarray[",p,"....",q,"]")

sumarray()
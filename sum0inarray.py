# given an aaray find the sum 0 is present or not in array
#input={3,4,-7,3,1,3,1,-4,-2,-2}

from array import *
def sumarray():
    c=0
    sum=0
    n=int(input("Enter the length of array"))
    arr=array('i',[])
    for i in range(n):
        p=int(input("Enter the value in array :"))
        arr.append(p)
    for i in range(n):
        for j in range(n):
            sum=sum+arr[j]
            if(sum==0):
                c=c+1

    if(c==0):print("No subarray with zero sum exist")
    else:print("subarray with zero sum exist")



sumarray()



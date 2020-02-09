# Find pair with given sum in the array
from array import *
def sum():
        c=0
        sum=int(input("Enter the value of sum "))
        n=int(input("Enter the length of array"))
        arr=array('i',[])
        for i in range(n):
            p=int(input("Enter the value in array :"))
            arr.append(p)
        for i in range(n):
            for j in range(i+1,n):
                if (arr[i]+arr[j]==sum):
                    print(i,j)
                    c=c+1
        if c==0:
            print("there is no match with the sum")

sum()
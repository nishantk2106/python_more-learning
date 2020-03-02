# Find pair with given sum in the array
from array import *
def sum(ar,arr_size,s):
    for i in range(arr_size):
        for j in range(i+1,arr_size):
            if (ar[i]+ar[j]==s):
                print(ar[i],ar[j])
    else:
            print("there is no match with the sum")
#
ar=[1,2,2,3,4,4,5,6,7,7]
s=10
arr_size=len(ar)
sum(ar,arr_size,s)

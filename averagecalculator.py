from array import *
def avg(arr,n):
    sum=0
    for i in range(n):
        sum=sum+arr[i]
    return sum/n
# driver code
if __name__=='__main__':
    arr=[2,3,4,5,6,7,8,9,10]
    n=len(arr)
    print(avg(arr,n))

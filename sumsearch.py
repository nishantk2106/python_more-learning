from array import *

def search(arr,sum):
    low = 0
    high = len(arr) - 1
    c = 0
    while low < high:
        if (arr[low] + arr[high] == sum):
            print(arr[low],arr[high])
            c=c+1
            low=low+1
        elif(arr[low]<arr[high]):high=high-1
        else:low=low+1
    if c == 0:
        print("there is no sum match with the array value")

    # driver code
if __name__=='__main__':
    sum = 0
    arr = [2,7,3,4,5,6,-7]
    search(arr,sum)


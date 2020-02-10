from array import *
def search():
    sum = int(input("Enter the value of sum "))
    n = int(input("Enter the length of array"))
    arr = array('i', [])
    for i in range(n):
        p = int(input("Enter the value in array :"))
        arr.append(p)
    low = 0
    high = n - 1
    c = 0
    while low < high:
        if (arr[low] + arr[high] == sum):
            print(low, high)
            c=c+1
            break
        if(arr[low]>arr[high]):high=high-1
        else:low=low-1
    if c == 0: print("there is no sum match with the array value")


search()

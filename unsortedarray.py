# The largest and smallest number in an unsorted integer array
def prinlargeandsmall(arr):
    n=len(arr)
    if n<2:print("invalid input")
    min,max=9999999,0
    for i in range(n):
        if (arr[i]<min):
            min=arr[i]
        if(arr[i]>max):
            max=arr[i]
    print(max,min)
# driver code
if __name__=='__main__':
    arr=[12,13,14,1,10,34,12]
    prinlargeandsmall(arr)

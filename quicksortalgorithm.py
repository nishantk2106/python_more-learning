# Sort an integer array in place using the QuickSort algorithm
# defining the partion function
def partition (arr,low,high):
    i=low-1
    pivot=arr[high]
    for j in range(low,high):
        if arr[j]<pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return(i+1)
# defining the quick sort function
def quicksort(arr,low,high):
    if low< high:
        pi= partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)

# driver code
arr=[1,40,100,50,30,80,10]
n=len(arr)
quicksort(arr,0,n-1)
print("Sorted array is :")
for i in range(0,n):
    print("%d"%arr[i])
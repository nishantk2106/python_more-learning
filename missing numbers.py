# Find a missing number in a given integer array of 1 to 10

def getmissingnum(arr,ar):
    total=3
    for i in range(4,ar+2):
        total+=i
        total-=arr[i-2]
    return total
# driver code :
arr=[1,2,3,5,6,7,8,9,10]
ar=len(arr)
print(getmissingnum(arr,ar))
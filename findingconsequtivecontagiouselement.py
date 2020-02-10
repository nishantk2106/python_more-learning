def max(x,y):
    return x if x>y else y
def min(x,y):
    return x if x<y else y
def findlength(arr,n):
    max_len=1
    for i in range(n-1):
        mn=arr[i]
        mx=arr[i]
        for j in range(i+1,n):
            mn=min(arr[i],arr[j])
            mx=max(arr[i],arr[j])
            if((mx-mn)==j-i):
                max_len=max(max_len,mx-mn+1)
    return max_len
# Driver Code
arr = [1, 56, 58, 57, 90, 92, 94, 93, 91, 45]
n = len(arr)
print("Length of the longest contiguous subarray is ",findlength(arr, n))
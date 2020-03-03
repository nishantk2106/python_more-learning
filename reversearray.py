def reverse (ar,arr_size):
    for i in range(arr_size-1,-1,-1):
        print(ar[i],end=" ")
# driver code
ar=[10,2,2,3,4,4,5,6,7,7,10]
arr_size=len(ar)
reverse(ar,arr_size)
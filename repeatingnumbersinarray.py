def repeatingnumber(arr,size):
    for i in range(size):
        if arr[abs(arr[i])]>0:
            arr[abs(arr[i])]=-arr[abs(arr[i])]
        else:
            print(abs(arr[i]),end=" ")

# driver code
ar=[1,2,2,3,4,4,5,6,7,7]
arr_size=len(ar)
repeatingnumber(ar,arr_size)
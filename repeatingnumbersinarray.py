def repeatingnumber(arr,size):
    for i in range(size):
        for j in range(i+1,size):
            if(arr[i]==arr[j]):
                print(arr[i],end=" ")

# driver code
ar=[1,2,2,3,4,4,5,6,7,7]
arr_size=len(ar)
repeatingnumber(ar,arr_size)
from array import *
def removingduplicate(arr):
    n=len(arr)
    a=array('i',[])
    for i in range(0,n):
        if arr[i] in a:continue
        a.append(arr[i])
    p=sorted(a)
    print(p)
# driver code
if __name__=='__main__':
    arr=[12,13,14,1,10,34,12,14]
    p=removingduplicate(arr)

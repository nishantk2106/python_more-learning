# How to check if two String is a rotation of each other
def rotation(x,y):
    l1=len(x)
    l2=len(y)
    temp=''
    if (l1!=l2):return 0
    temp=x+x
    if (temp.count(y)>0):return 1
    else:return 0
# driver code
if __name__=="__main__":
    x="ABCD"
    y="CDAB"
    if rotation(x,y):
        print("String are rotation of each other ")
    else :
        print("String is not rotation of each other ")


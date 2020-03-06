# How to reverse a given String using recursion
def reverse_recurse(x):
    a=0
    if(len(x)==0):
        return
    temp=x[0]
    reverse_recurse(x[1:])
    print(temp,end=" ")
# driver code
if __name__=="__main__":
    x="nishant"
    print(x[::-1])
    p=reverse_recurse(x)

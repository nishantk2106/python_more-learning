 # How to print first non repeated character from String
def nonrepeat(x):
    d=dict()
    for i in x:
        if i not in d:d[i]=1
        else:d[i]+=1
    for p,q in d.items():
        if (q==1):
            print(p)
            break;
# driver code
if __name__=="__main__":
    x=input("Enter the string and find the first non repeatative character :")
    nonrepeat(x)

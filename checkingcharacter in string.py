# How to count the occurrence of a given character in String?
def occurance(x,y):
    c=0
    for p in y:
        if x != p:continue
        c=c+1
    if (c==0):print("No occurance of character in the string")
    else :print(c)


# driver code
if __name__=="__main__":
    x=input("Enter the character you want to check in string :")
    y=input("Enter the string :")
    occurance(x,y)
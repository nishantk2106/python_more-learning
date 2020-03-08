# How to reverse words in a given sentence without using any library method?
def rev(x):
    temp=""
    for i in x :
        if i not in " ":temp=i+temp
        else:
            print(temp)
            temp=""
# driver code
if __name__=="__main__":
    x=input("Enter the string :")
    rev(x)
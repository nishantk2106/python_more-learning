 # How to check if a String contains only digits?

def check(x):
 try:
     p=int(x)
     print("string contains only digit")
 except:
     print("String does not contains only digit")

# driver code:

if __name__=="__main__":
    x=input("Enter the string :")
    check(x)
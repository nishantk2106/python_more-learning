 # How to check if given String is Palindrome?
def palindrome(x):
    if (x==x[::-1]):
        print("palindrome")
    else:
        print("not palindrome")
# driver code
if __name__=="__main__":
    x=input("enter the String for palindrome :")
    palindrome(x)
# How to find all permutations of String
from itertools import permutations
def permut (x):
    temp=permutations(x)
    for i in temp:
        print(''.join(i))
# driver code
if __name__=="__main__":
    x=input("Enter the string :")
    permut(x)
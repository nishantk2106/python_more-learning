 # How to count a number of vowels and consonants in a given String?
def vowel_cons_count(x):
    v,c=0,0
    for i in x:
        if (i=='a'or i=='e' or i=='i' or i=='o'or i=='u'):v=v+1
        else:c=c+1
    print("The total number of consonant in string :",c)
    print("The total number of vowel in the string :",v)

# driver code
if __name__=="__main__":
     x=input("Enter the string:")
     p=x.lower()
     vowel_cons_count(p)
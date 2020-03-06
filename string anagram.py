# How to check if two Strings are anagrams of each other?
def anagram(x,y):
    if (sorted(x)==sorted(y)):
        print("Anagram")
    else:print("not anagram")

# driver code
if __name__=="__main__":
    x="silent"
    y="listen"
    anagram(x,y)
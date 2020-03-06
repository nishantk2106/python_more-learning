# How to Print duplicate characters from String?
def duplicate(x):
    d=dict()
    for word in x:
        if word not in d:d[word]=1
        else :d[word]+=1
    return d
# driver code
if __name__=="__main__":
    x=input("Enter the String to find the duplicate character :")
    p=duplicate(x)
    for q,r in p.items():
        if(r>=2):
            print(q)





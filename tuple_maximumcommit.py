lst=list()
d=dict()
try:
    fhand=open("mbox.txt",'r')
except:
    print("cannot find the file in directory ")
    exit()
for lines in fhand:
    lines=lines.rstrip()
    if lines.startswith("From:"):
        word=lines.split()
        word=word[1]
        if word not in d:d[word]=1
        else:d[word]+=1
for key,val in list(d.items()):
    lst.append((val,key))
lst.sort(reverse=True)
for k,v in lst:
    print(v,k)
    break

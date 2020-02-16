# Add code to the above program to figure out who has the most
# messages in the file.
x=input("Enter the file name :")
try :
    fhand=open(x)
except:
    print("the file cannot be opened :",x)
    exit()
count=dict()
for lines in fhand:
    lines=lines.rstrip()
    lines=lines.lower()
    if not lines.startswith('from '):continue
    p=lines.split()
    print(p)
    if p[1] not in count:count[p[1]]=1
    else:count[p[1]]+=1
    print(max(count,key=count.get),max(count.values()))
# print(max(zip(count.values(),count.keys())))
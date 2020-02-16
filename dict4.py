# Write a program to read through a mail log, build a histogram using
# a dictionary to count how many messages have come from each email address, and
# print the dictionary.
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
print(count)

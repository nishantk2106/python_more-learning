 # Write a program that categorizes each mail message by which day of
# the week the commit was done. To do this look for lines that start with “From”,
# then look for the third word and keep a running count of each of the days of the
# week. At the end of the program print out the contents of your dictionary (order
# does not matter).
from string import *
x=input("Enter the file name :")
try :
    fhand=open(x)
except:
    print("the file cannot be opened :",x)
    exit()
count=dict()
for lines in fhand:
    lines=lines.rstrip()
    if not lines.startswith('From '):continue
    p=lines.split()
    if p[2] not in count:count[p[2]]=1
    else:count[p[2]]+=1
print(count)
# Write a Python program to read through the lines of the file, break each
# line into a list of words, and then loop through each of the words in the line and
# count each word using a dictionary considering the diffrent type of punctuation
from string import *
x=input("Enter the file name :")
try:
    fhand=open(x)
except:
    print("File cannot be opened :",x)
    exit()
count=dict()
for lines in fhand:
    lines=lines.rstrip()
    lines=lines.translate(lines.maketrans('','',punctuation))
    lines=lines.lower()
    word=lines.split()
    for i in word:
        if i not in count:
            count[i]=1
        else:
            count[i]+=1
print(count)
# Write a Python program to read through the lines of the file, break each
# line into a list of words, and then loop through each of the words in the line and
# count each word using a dictionary.
x=input("enter the file name :")
try:
    fhand=open(x)
except:
    print("file cannot be opened :",x)
    exit()
d = dict()
for line in fhand:
    word=line.split()
    for c in word:
        d[c]=d.get(c,0)+1
print(d)
# Exercise 2: Write a program to look for lines of the form
# `New Revision: 39772`
# and extract the number from each of the lines using a regular expression and
# the findall() method. Compute the average of the numbers and print out the
# average.
import re
sum=0
c=0
fhand=open("mbox-short.txt")
for lines in fhand:
    lines=lines.rstrip()
    x=re.findall('^New.*([0-9]{5})',lines)
    if len(x)>0:
        for a in x:
            sum=sum+int(a)
            c=c+1
print(sum/c)
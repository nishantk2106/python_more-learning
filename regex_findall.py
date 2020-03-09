import re
hand = open('mbox.txt')
for line in hand:
    line = line.rstrip()
    x= re.findall('\S+@\S+', line)
    if len(x)>0:
        print(x)
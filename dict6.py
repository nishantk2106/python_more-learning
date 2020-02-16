# This program records the domain name (instead of the address) where
# the message was sent from instead of who the mail came from (i.e., the whole email
# address). At the end of the program, print out the contents of your dictionary.
from string import punctuation
x=input("Enter the name of the file :")
try:
    fhand=open(x)
except:
    print("the file cannot be opened :",x)
count=dict()
for line in fhand:
    line=line.rstrip()
    line=line.lower()
    if not line.startswith('from '):continue
    # line=line.translate(line.maketrans('@',' '))
    line=line.split()
    email=line[1]
    domain=email.split('@')[1]
    print(domain)
    if domain not in count:count[domain]=1
    else: count[domain]+=1
print(count)
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
x=handle.read()
a=[]
c=dict()
for line in handle:
    if not line.startswith("From "):
        
        continue
    if line.startswith("From"):
        y=line.split()
        a.append(y[1])
        
#print(a)
for mail in a:
    if mail not in c:
        c[mail]=1
    else:
        c[mail]=c[mail]+1
'''  c[mail]=c.get(mail,0)+1
      '''
#print(c)
big=None
for word,s in c.items():
    if big is None or s>big:
        big=s
        bigword=word
print(bigword,big)

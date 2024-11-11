file=open('JEE.txt','r')

for line in file:
    words=line.split()
    for word in words:
        print(word)

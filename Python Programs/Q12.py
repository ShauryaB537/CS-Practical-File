from pickle import load, dump
import os
def binw():
    f=open('pqr.txt' , 'wb')
    while True:
        s=[]
        r=int(input("Enter roll: "))
        n=input("Enter name: ")
        s.append(r)
        s.append(n)
        dump(s,f)
        q=input("Continue (y/n): ")
        if q=="n":
            break
    f.close()

def modr():
    s1=[]
    s=[]
    f=open('pqr.txt' , 'rb')
    f1=open('stu.txt' , 'wb')
    x=int(input("Enter roll to be changed: "))
    y=input("Enter modified value: ")
    s.append(x)
    s.append(y)
    try:
        while True:
            s1=load(f)
            if s1[0]==x:
                dump(s, f1)
            else:
                dump(s1, f1)
    except EOFError:
        print("Record Updated")
    f.close()
    f1.close()
    os.remove('pqr.txt')
    os.rename('stu.txt','pqr.txt')

binw()
modr()

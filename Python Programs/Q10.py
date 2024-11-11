f=open("YouAreMySunshine.txt","r")
x=f.readlines()

L=[]

n1=int(input("Enter no. of lines you want to select: "))

for a in range(n1):
    n=int(input("Line number of selected line: "))
    y=x[n-1]
    L.append(y)

f.close()
f=open("MyOnlySunshine.txt","w+")
f.writelines(L)
f.close()
print("Lines duplicated successfully")

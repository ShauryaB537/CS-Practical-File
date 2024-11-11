import csv
def csv_writerows():
    f=open('empl.csv', 'w', newline='')
    cur=csv.writer(f)
    a=["Name", "Empl Code"]
    cur.writerow(a)
    while True:
        s=[]
        n=input("Name: ")
        j=input("Empl Code: ")
        s.append(n)
        s.append(j)
        cur.writerow(s)
        q=input("Continue (y/n): ")
        if q=="n":
            break
    print("\n New CSV File Created")
    f.close()

def csv_searchrec():
    f=open('empl.csv' , 'r', newline='')
    cur=csv.reader(f)
    next(cur)
    y=input("Enter value to be searched: ")
    try:
        for r in cur:
            if r[1]==y:
                print(r)
    except EOFError:
        print("End of file")


csv_writerows()
csv_searchrec()

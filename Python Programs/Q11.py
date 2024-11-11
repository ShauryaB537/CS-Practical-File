from pickle import load, dump

file = open('binary.txt', 'wb')
s = []

print('\nENTER NAME AND ROLL NO.')
while True:
    n = input('Name: ')
    r = int(input('Roll No: '))
    s.append(n)
    s.append(r)
    dump(s, file)
    s = []
    q = input('Do you want to add more records (y/n): ')
    if q != 'y':
        break
file.close()

file = open('binary.txt', 'rb')
s1 = []
i = int(input('Enter roll no to be searched: '))

try:
    while True:
        s1 = load(file)
        if s1[1] == i:
            print(s1)
except EOFError:
    print('End of File')
file.close()

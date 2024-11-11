import pickle
file = open('records.dat', 'wb')
record=[{'id': 1, 'name': 'Shaurya', 'age': 17, 'department': 'IT'}]
pickle.dump(record, file)

file = open('records.dat', 'rb')
records=pickle.load(file)
print(records)

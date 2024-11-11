import pickle

records=[]
while True:
    print("\nEnter record details:")

    record_id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    department = input("Enter Department: ")

    record = {"id": record_id, "name": name, "age": age, "department": department}
    records.append(record)

    more = input("Do you want to add another record? (yes/no): ").lower()
    if more != "yes":
        break

file = open('records.dat', 'wb')
pickle.dump(records, file)
print(f"Records have been written.")

def search_record(search_id):
    try:
        file = open('records.dat', 'rb')
        records = pickle.load(file)
        for record in records:
            if record['id'] == search_id:
                print("Record found:")
                print(record)
                return
            print(f"Record with ID {search_id} not found.")
    except:
        pass

search_id = int(input("Enter the ID of the record to search for: "))
search_record(search_id)

#WHY IS THIS NOT WORKING??

import pymysql as x

def connect():
    try:
        global y
        y = x.connect(host='localhost', user='root', passwd='123456', db='pymysql')
        global cur
        cur = y.cursor()
    except Exception as e:
        print(e)

def execute_query(query):
    try:
        cur.execute(query)
        y.commit()
        results = cur.fetchall()
        for result in results:
            print(result)
    except Exception as e:
        print(e)

def main_menu():
    while True:
        print("\nMain Menu")
        print("1. See tables")
        print("2. See data in a table")
        print("3. See an existing record in an existing table")
        print("4. Create a record in an existing table")
        print("5. Alter a record in an existing table")
        print("6. Exit")
        n = int(input("\nEnter your choice: "))
        if n == 1:
            query = "SHOW TABLES;"
            execute_query(query)
        elif n == 2:
            table_name = input("\nEnter name of table: ")
            query = f"SELECT * FROM {table_name};"
            execute_query(query)
        elif n == 3:
            table_name = input("\nEnter name of table: ")
            column_name = input("\nEnter the type of data of record holder, e.g., 'MovieID' or 'Title': ")
            record = input("\nEnter data of record holder: ")
            query = f"SELECT * FROM {table_name} WHERE {column_name} = '{record}';"
            execute_query(query)
        elif n == 4:
            add_records()
        elif n == 5:
            update_record()
        elif n == 6:
            cur.close()
            y.close()
            break

def add_records():
    num_records = int(input("Enter number of records you want to add: "))
    for _ in range(num_records):
        table_name = input("\nEnter name of table: ")
        movie_id = input("Movie ID: ")
        title = input("Title: ")
        genre = input("Genre: ")
        director = input("Director: ")
        release_year = input("Release Year: ")
        price = input("Price: ")
        quantity = input("Quantity: ")
        description = input("Description: ")
        query = f"INSERT INTO {table_name} VALUES ({movie_id}, '{title}', '{genre}', '{director}', {release_year}, {price}, {quantity}, '{description}');"
        execute_query(query)

def update_record():
    table_name = input("\nEnter name of table: ")
    old_data = input("\nEnter data to be updated: ")
    new_data = input("\nEnter new data: ")
    column_name = input("\nEnter field to be updated: ")
    query = f"UPDATE {table_name} SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}';"
    execute_query(query)

connect()
main_menu()

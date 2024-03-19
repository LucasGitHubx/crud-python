from db.db import DB

def crudFunctions(option):
    db = DB()
    
    if option == 1:
        db.select()
    elif option == 2:
        try:
            name = input("Type the name of the course you want to create: ")
            capacity = int(input("Type the capacity of the course you want to create:"))
            date = input("Type the course's creation date (YYYY-MM-DD): ")

            db.insert(name, capacity, date)
        except Exception as e:
            print(e)
    elif option == 3:
        try:
            id = int(input("Type the id of the course you want to update: "))
            name = input("Type the name of the course: ")
            capacity = int(input("Type the capacity of the course: "))
            date = input("Type the course's creation date (YYYY-MM-DD): ")

            db.update(id, name, capacity, date)
        except Exception as e:
            print(e)
    else:
        try:
            id = int(input("Type the id of the course you want to delete: "))

            db.delete(id)
        except Exception as e:
            print(e)


def menu():
   while  True:
       print("\n==== MYSQL CRUD ====")
       print("1. Select courses. ")
       print("2. Insert courses. ")
       print("3. Update courses. ")
       print("4. Delete courses. ")
       print("0. Exit")

       option = int(input("Select a number:"))
       if option<0 or option>4:
           print("You put a wrong number. Type again...")
       elif option==0:
           print("Thanks for using the system.")
           break
       else:
           crudFunctions(option)

menu()
DB = open("database.log", "a+")

def set (key, value):
        DB.write(key + ": " + value + "\n")

def close_db():
     DB.close()

def get(key):
    DB.seek(0)
    latest_value = None
    for line in DB:
        line = line.strip()
        stored = line.split(": ", 1)
        if len(stored) != 2:
            continue
        else:
            stored_key = stored[0]
            stored_value = stored[1]
            if stored_key == key:
                if stored_value == "deleted":
                    latest_value = None
                else:
                    latest_value = stored_value
    if latest_value is None:
        print("key not found")
    else:
        print(latest_value)


def delete(key):
    exists = False
    DB.seek(0)
    for line in DB:
         line = line.strip()
         stored = line.split(": ", 1)
         if len(stored) != 2:
            continue
         else:
            stored_key = stored[0]
            stored_value = stored[1]
            if stored_key == key:
                if stored_value == "deleted":
                    exists = False
                else:
                    exists = True
    if exists:
        DB.write(key + ": deleted \n")
        print("key deleted successfully")
    else:
        print("Key not found")

         


while True:
    User_input = input("\n input command: ")

    parts = User_input.split( maxsplit=2)

    if len(parts) == 0:
         print("Please input a command")
         continue
    command = parts[0].lower()
    

    if command == "set":
        if len(parts) == 3:
            key = parts[1]
            value = parts[2]
            set(key, value)
            print(key, "added successfully")
        else:
            print("Invalid SET syntax")
            
    elif command == "get":
        if len(parts) == 2:
            key = parts[1]
            get(key)
        else:
            print("Invalid GET syntax")
            

    elif command == "delete":
        if len(parts) == 2:
            key = parts[1]
            delete(key)
        else:
            print("Invalid DELETE syntax")
            
    elif command == "exit":
        if len(parts) == 1:
            close_db()
            break
        else:
             print("Invalid EXIT syntax")
    else:
        print("Please use the commands and their proper syntax") 
         
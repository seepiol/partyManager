import sqlite3
import random
import string

dbname = "party.db"

conn = sqlite3.connect(dbname)
c = conn.cursor()

codes = []

def make_tables():
    print("Initializing DB")
    try:
        c.execute("""CREATE TABLE people
                    (id integer primary key autoincrement, code text, name text, surname text)""")
        
        c.execute("""CREATE TABLE items
                    (id integer primary key autoincrement, name text, outOfStock integer)""")
        
        conn.commit()
        print("DB initialized")
    except sqlite3.OperationalError:
        print(f"The database \"{dbname}\" already exists.")

def generate_code(length):
    letters = string.ascii_lowercase
    code = ''.join(random.choice(letters) for i in range(length))
    while code in codes:
        code = ''.join(random.choice(letters) for i in range(length))
    codes.append(code)
    return code

def populate_people():
    complete_name = input("Insert name and surname (RETURN to end): ")
    while complete_name != "":
        name = complete_name.split(" ")[0]
        surname = complete_name.split(" ")[1:]
        surname = " ".join(surname)
        c.execute("INSERT INTO people VALUES (NULL,?,?,?)", (generate_code(4), name, surname))
        complete_name = input("Insert name and surname (RETURN to end): ")
    conn.commit()

def populate_items():
    #TODO
    pass
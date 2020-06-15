"""
    PartyManager:
    WebApp for ordering beverages and other stuff written in flask
    Copyright (C) 2020 

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""

import sqlite3
import random
import string

dbname = "party.db"

conn = sqlite3.connect(dbname, check_same_thread=False)
c = conn.cursor()

codes = []

def make_tables():
    print("Initializing DB")
    try:
        c.execute("""CREATE TABLE people
                    (id integer primary key autoincrement, code text, name text, surname text)""")
        
        c.execute("""CREATE TABLE items
                    (id integer primary key autoincrement, name text, outOfStock integer)""")
        '''
        c.execute("""CREATE TABLE orders
                    (id integer primary key autoincrement, item text, person text""")
        conn.commit()
        '''
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
    item_name = input("Insert the item name (RETURN to end): ")
    while item_name != "":
        c.execute("INSERT INTO items VALUES (NULL,?,0)", (item_name,))
        item_name = input("Insert the item name (RETURN to end): ")
    conn.commit()

def find_person(code):
    c.execute("SELECT name, surname FROM people WHERE code=?", (code,))
    result = c.fetchall()
    return " ".join(result[0])

def display_items():
    c.execute("SELECT name, outOfStock FROM items")
    result = c.fetchall()
    return result
"""
def save_order(item, person):
    c.execute("INSERT INTO orders VALUES (NULL, ?, ?)", (item, person))
    conn.commit()
"""
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
    """
    Creates the tables in the sqlite3 database
    
    Table 'people': id, code, name, surname
    Table 'items': id, name, orders, outOfStock
    Table 'orders': id, item, person

    """
    print("Initializing DB")
    try:
        c.execute("""CREATE TABLE people
                    (id integer primary key autoincrement, code text, name text, surname text)""")
        
        c.execute("""CREATE TABLE items
                    (id integer primary key autoincrement, name text, orders integer, outOfStock integer)""")

        c.execute("""CREATE TABLE orders
                    (id integer primary key autoincrement, item text, person text)""")
        conn.commit()

        print("DB initialized")

    except sqlite3.OperationalError:
        print(f"The database \"{dbname}\" already exists.")

def generate_code(length):
    """
    Creates a random code of n alphabetical characters.
    Checks that it is not already present in 'codes' list

    Args:
        lenght (int): number of the characters
    
    Returns:
        code (str): the n characters code

    """
    letters = string.ascii_lowercase
    code = ''.join(random.choice(letters) for i in range(length))
    while code in codes:
        code = ''.join(random.choice(letters) for i in range(length))
    codes.append(code)
    return code

def check_code(code):
    c.execute("SELECT * FROM people WHERE code=?", (code,))
    result = c.fetchall()
    if len(result) == 0:
        return False
    else:
        return True

def find_person(code):
    """
    Search for a match between a code provided as argument and a person in the database

    Args:
        code (str): the 4 characters code 
    
    Returns:
        complete_name (str): complete name of the person corresponding to the code
    
    If there isn't a match: 
    Returns False

    """
    c.execute("SELECT name, surname FROM people WHERE code=?", (code,))
    result = c.fetchall()
    complete_name = " ".join(result[0])
    return complete_name

def display_items():
    """
    Displays the items in the database
    
    Returns:
        result (list): a list containing the id, the item name and its status (if it's out of stock or not)

    """
    c.execute("SELECT * FROM items")
    result = c.fetchall()
    return result

def save_order(item, code):
    """
    Save the order in the database

    Args:
        item (str): the name of the item
        code (str): the code of the person

    """
    if check_code(code) and check_item(item):
        c.execute("INSERT INTO orders VALUES (NULL, ?, ?)", (item, find_person(code)))
        c.execute("UPDATE items SET orders = orders + 1 WHERE name=?", (item,))
        conn.commit()
    else:
        return 0
    
def make_out_of_stock(id):
    """
    makes an item out of stock

    Args:
        id (int): the id of the item

    """
    c.execute("UPDATE items SET outOfStock = 1 WHERE id = ?", (id,))
    conn.commit()

def check_item(item):
    """
    check if an item exists

    Args:
        item (str): the name of the item

    Returns:
        if exists:
            True (bool)
        if doesn't exists:
            False (bool)

    """
    c.execute("SELECT * FROM items WHERE name=? AND outOfStock=0", (item,))
    r = c.fetchall()
    if len(r) == 0:
        return False
    else:
        return True

def add_person(complete_name):
    """
    add a person in the db with the unique 4 chars code

    Args:
        complete_name (str): the name and surname of the person

    """
    name = complete_name.split(" ")[0]
    surname = complete_name.split(" ")[1:]
    surname = " ".join(surname)
    c.execute("INSERT INTO people VALUES (NULL,?,?,?)", (generate_code(4), name, surname))
    conn.commit()

def add_item(item_name):
    """
    Add an item in the db

    Args:
        item_name (str): the name of the item

    """
    c.execute("INSERT INTO items VALUES (NULL, ?, 0, 0)", (item_name,))
    conn.commit()


def print_people():
    """
    Select all the people 

    Returns:
        c.fetchall() (list): the result of the SQL query

    """
    c.execute("SELECT code, name, surname FROM people")
    return c.fetchall()


def get_order(i):
    """
    Select a precise order

    Args:
        i (int): the id of the order
    
    Results:
        c.fetchone() (list): the result of the SQL query

    """
    c.execute("SELECT item, person FROM orders WHERE id=?", (i,))
    return c.fetchone()

# Dashboard Methods

def get_total_order():
    c.execute("SELECT * FROM orders")
    return len(c.fetchall())

def get_favourite_item():
    c.execute("SELECT item, COUNT(item) as n FROM orders GROUP BY item ORDER BY n DESC LIMIT 1")
    try:
        return c.fetchall()[0][0]
    except IndexError:
        return None


def get_available_item():
    c.execute("SELECT * FROM items WHERE outOfStock = 0")
    av = len(c.fetchall())
    c.execute("SELECT * FROM items")
    tot = len(c.fetchall())
    return f"{av}/{tot}"

def get_active_users():
    c.execute("SELECT DISTINCT person FROM orders")
    return len(c.fetchall())
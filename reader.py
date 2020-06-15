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


i = 1

while True:
    try:
        c = conn.cursor()
        c.execute("SELECT item, person FROM orders WHERE id=?", (i,))
        r = c.fetchall()
        print(len(r), r)
        if len(r) == 0:
            print("no other orders...")
            pass
        else:
            i+=1
        c.close()
        input()
    except:
        pass
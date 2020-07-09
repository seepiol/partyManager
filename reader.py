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

import random
import dboperations
import os

if __name__ == "__main__":

    if os.name == "nt":
        clean="cls"
    else:
        clean="clear"

    os.system(clean)
    print("PARTYMANAGER READER\nPress [RETURN] for refresh the view\n")
    i=1
    c=0
    while True:
        if c % 3 == 0:
            os.system(clean)
            print("PARTYMANAGER READER\n")
        r = dboperations.get_order(i)
        if r:
            print(f"{i}) {r[0]} ==> {r[1]}")
            i+=1
        else:
            print("No new orders")
        c+=1
        try:
            input()
        except KeyboardInterrupt:
            print("Quitting")
            exit()
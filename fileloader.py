"""
    PartyManager:
    WebApp for ordering beverages and other stuff written in flask
    Copyright (C) 2020 

    This program is free software: you can redistribute it and/or modify
    it under the terms of thTotal visits: {{visits}} - Errors: {{errors}} - e GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""

from tkinter import Tk
from tkinter.filedialog import askopenfilename
import csv
import dboperations
import argparse

def load_people(people_list):
    for person in people_list:
        if person[0] == "X":
            print(f"- ignored {person}")
        else:
            dboperations.add_person(person)
            print(f"- added {person}")

def load_items(items_list):
    for item in items_list:
        if item[0] == "X":
            print(f"- ignored {item}")
        else:
            dboperations.add_item(item)
            print(f"- added {item}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Rasp2Pc PC Component")
    parser.add_argument(
        "-f","--filename",
        type=str,
        default="",
        help="the .csv filename",
    )

    parser.add_argument(
        "-t","--type",
        type=str,
        help="The information contained in the csv file ('people' or 'items')",
    )

    args = parser.parse_args()

    print("PartyManager FileLoader")
    print("Program to load the information (people or items) contained in a csv file into the database")

    if not args.type:
        table = input("What information does the csv contain?\n1) People List\n2) Item List\n> ")
        while table not in ("1", "2"):
            table = input("What information does the csv contain?\n1) People List\n2) Item List\n> ")
    else:
        table=args.type

        if table in ("p","people","1"):
            table="1"
        elif table in ("i","item","items","2"):
            table="2"

    if not args.filename:
        Tk().withdraw()
        input("Please press return and select the csv file. Please make sure that the file extention is .csv\n > ")
        filename = askopenfilename(title="Select CSV file", filetypes=(("csv files","*.csv"),("all files","*.*")) )
    else:
        filename=args.filename

    info_list = []

    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            info_list.append(row)
        
    if table == "1":
        load_people(info_list[0])
    
    elif table == "2":
        load_items(info_list)

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

# Libs
from flask import Flask, render_template, request, redirect
import os
import sqlite3
import dboperations
import csv

app=Flask(__name__)

# Main Route
@app.route("/")
def index():
    arg_code = request.args.get("code")
    return render_template("index.html", items = dboperations.display_items(), code=arg_code)

# Making Order
@app.route("/makeorder", methods=["POST"])
def makeorder():
    # Getting the values
    code = request.form.get("code")
    item = request.form.get("item")
    arg_code = request.args.get("code")

    if not code and arg_code != "":
        code = arg_code

    if not item:
        return render_template("goback.html", message="Please select an item", code=code)

    if not code and not arg_code:
        return render_template("goback.html", message="Please insert your code")
    
    
    person = dboperations.find_person(code)
    if person == False:
        return render_template("goback.html", message="Unvalid code")
    dboperations.save_order(item, person)
    print(f"{person}->{item}")

    return render_template('success.html', name=person, code=code)

# MAIN
if __name__ == '__main__':
    dboperations.make_tables()
    app.debug = True
    app.run(host = '0.0.0.0', port=8081)

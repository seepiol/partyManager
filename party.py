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
    return render_template("index.html", items = dboperations.display_items())

# Making Order
@app.route("/makeorder", methods=["POST"])
def makeorder():
    # Getting the values
    code = request.form.get("code")
    item = request.form.get("item")
    if not item or not code:
        print("Not all form completed")
        return 'Please complete all input forms. <a href="/">Go Back</a>'

    person = dboperations.find_person(code)
    if person == False:
        return 'Unvalid Code. <a href="/">Go Back</a>'
    dboperations.save_order(item, person)
    print(f"{person}->{item}")

    return render_template('success.html')

# MAIN
if __name__ == '__main__':
    dboperations.make_tables()
    app.debug = True
    app.run(host = '0.0.0.0', port=8080)

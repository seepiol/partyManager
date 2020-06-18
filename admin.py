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

# Libs
from flask import Flask, render_template, request, redirect, url_for
import os
import sqlite3
import dboperations
import csv
import datetime

app=Flask(__name__)

visits = 0
errors = 0
start_time = datetime.datetime.now()

# Main Route
@app.route("/")
def index():
    global visits
    visits+=1
    arg_code = request.args.get("code")
    return render_template("admin.html", items = dboperations.display_items_id(), code=arg_code)

@app.route("/addperson", methods=["POST"])
def add_person():
    person_name = request.form.get("personName")
    dboperations.add_person(person_name)
    return redirect("/")

@app.route("/additem", methods=["POST"])
def add_item():
    item_name = request.form.get("itemName")
    dboperations.add_item(item_name)
    return redirect("/")

@app.route("/outofstock", methods=["POST"])
def out_of_stock():
    id = request.form.get("itemName")
    dboperations.make_out_of_stock(id)
    return redirect("/")


# ERROR PAGES

@app.route("/404")
@app.errorhandler(404)
def not_found(a):
    global errors
    errors+=1
    arg_code = request.args.get("code")
    return render_template('error.html', code=arg_code, error_code="404", error_message="We're sorry, the page you're searching doesn't exists"), 404

@app.route("/405")
@app.errorhandler(405)
def method_not_allowed(a):
    global errors
    errors+=1
    arg_code = request.args.get("code")
    return render_template('error.html', code=arg_code, error_code="405", error_message="We're sorry, the requested method isn't allowed"), 405

@app.route("/500")
@app.errorhandler(500)
def internal_server_error(a):
    global errors
    errors+=1
    print("ERROR 500, WARNING")
    arg_code = request.args.get("code")
    return render_template('error.html', code=arg_code, error_code="500", error_message="We're sorry, the server has encountered a unknown situation. The developer has been warned"), 500

@app.route("/503")
@app.errorhandler(503)
def service_unavailable(a):
    global errors
    errors+=1
    print("ERROR 503, WARNING")
    arg_code = request.args.get("code")
    return render_template('error.html', code=arg_code, error_code="503", error_message="We're sorry, the service is unavailable. Please wait a moment and try again. The developer has been warned"), 503


# MAIN
if __name__ == '__main__':
    dboperations.make_tables()
    app.debug = True
    app.run(host = '127.0.0.1', port=5000)

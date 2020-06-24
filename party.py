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
    try:
        return render_template("index.html", items = dboperations.display_items(), code=arg_code)
    except sqlite3.ProgrammingError:
        return render_template("goback.html", message="Something went wrong", code=arg_code)

@app.route("/policy")
def policy():
    global visits
    visits+=1
    arg_code = request.args.get("code")
    return render_template("policy.html", code=arg_code)

@app.route("/license")
def license():
    global visits
    visits+=1
    arg_code = request.args.get("code")
    return render_template("license.html", code=arg_code)

# Making Order
@app.route("/makeorder", methods=["POST"])
def makeorder():
    global visits
    visits+=1
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
    
    code=code.lower()

    person = dboperations.find_person(code)
    if person == False:
        return render_template("goback.html", message="Unvalid code")

    if not dboperations.item_exists(item):
        return render_template("goback.html", message="Unvalid or unavailable item", code=code)

    dboperations.save_order(item, person)

    try:
        return render_template('success.html', name=person, code=code)
    except sqlite3.ProgrammingError:
        return render_template("goback.html", message="Something went wrong", code=arg_code)

@app.route("/dash")
def dash():
    global visits
    global errors
    global start_time
    timedelta = ((datetime.datetime.now()-start_time).seconds)
    uptime = round(timedelta/60, 0)
    try:
        return render_template("dashboard.html", total_orders=dboperations.get_total_order(), favourite_item=dboperations.get_favourite_item(), active_users=dboperations.get_active_users(), available_items=dboperations.get_available_item(), time=5, visits=visits, errors=errors, uptime=int(uptime))
    except sqlite3.ProgrammingError:
        return render_template("goback.html", message="Something went wrong")
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
    app.run(host = '0.0.0.0', port=8080)

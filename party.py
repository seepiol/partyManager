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
from flask import Flask, render_template, request, redirect, url_for
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

@app.route("/policy")
def policy():
    arg_code = request.args.get("code")
    return render_template("policy.html", code=arg_code)

@app.route("/license")
def license():
    arg_code = request.args.get("code")
    return render_template("license.html", code=arg_code)

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

    if not dboperations.item_exists(item):
        return render_template("goback.html", message="Unvalid item", code=code)

    dboperations.save_order(item, person)
    print(f"{person}->{item}")

    return render_template('success.html', name=person, code=code)

@app.route("/dash")
def dash():
    return render_template("dashboard.html", total_orders=dboperations.get_total_order(), favourite_item=dboperations.get_favourite_item(), active_users=dboperations.get_active_users(), available_items=dboperations.get_available_item(), time=5)

# ERROR PAGES

@app.route("/404")
@app.errorhandler(404)
def not_found():
    arg_code = request.args.get("code")
    return render_template('error.html', code=arg_code, error_code="404", error_message="We're sorry, the page you're searching doesn't exists")

@app.route("/405")
@app.errorhandler(405)
def method_not_allowed():
    arg_code = request.args.get("code")
    return render_template('error.html', code=arg_code, error_code="405", error_message="We're sorry, the requested method isn't allowed")

@app.route("/500")
@app.errorhandler(500)
def internal_server_error():
    print("ERROR 500, WARNING")
    arg_code = request.args.get("code")
    return render_template('error.html', code=arg_code, error_code="500", error_message="We're sorry, the server has encountered a unknown situation. The developer has been warned")

@app.route("/503")
@app.errorhandler(503)
def service_unavailable():
    print("ERROR 503, WARNING")
    arg_code = request.args.get("code")
    return render_template('error.html', code=arg_code, error_code="503", error_message="We're sorry, the service is unavailable. Please wait a moment and try again. The developer has been warned")


# MAIN
if __name__ == '__main__':
    dboperations.make_tables()
    app.debug = True
    app.run(host = '0.0.0.0', port=8081)

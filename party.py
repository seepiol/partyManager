# Libs
from flask import Flask, render_template, request, redirect
import os
import sqlite3
import dboperations

app=Flask(__name__)


item_list = ["Birra","Coca-Cola","Pepsi"]
people_dict = {"a0a0":"Bob","ct01":"Alice"}

# Main Route
@app.route("/")
def index():
    return render_template("index.html", item_list = item_list)

# Making Order
@app.route("/makeorder", methods=["POST"])
def makeorder():
    # Getting the values
    code = request.form.get("code")
    item = request.form.get("item")
    if not item or not code:
        print("Not all form completed")
        return 'Please complete all input forms. <a href="/">Go Back</a>'
        
    if item not in item_list:
        print("Data selected not in list")
        return 'Unvalid data. <a href="/">Go Back</a> and input valid data'

    if code not in people_dict:
        print("Data selected not in list")
        return 'Unvalid data. <a href="/">Go Back</a> and input valid data'
    
    print(f"{people_dict.get(code)} -> {item}")

    return render_template('success.html')

# ERRORS

# Error 404
@app.errorhandler(404) 
def e404(e):
    return render_template("404.html")

# Error 405
@app.errorhandler(405) 
def e405(e):
    return render_template("405.html")

# Error 500
@app.errorhandler(500) 
def e500(e):
    return render_template("500.html")

# MAIN
if __name__ == '__main__':
    dboperations.make_tables()
    
    """
    decision = input("Do you want to populate the people list? <y/N>: ")
    if decision in ["y", "Y", "yes"]:
        dboperations.populate_people()
    else:
        pass

    decision = input("Do you want to populate items list? <y/N>: ")
    if decision in ["y", "Y", "yes"]:
        dboperations.populate_items()
    else:
        pass
    """
    
    app.debug = True
    app.run(host = '0.0.0.0', port=8080)

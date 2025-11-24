# -*- coding: utf-8 -*-
""" The program uses flask and runs a web server. 
When requesting this server, it returns the text "Hello World!"""
from flask import Flask, request
import sqlite3

# Creating a web application object:
app = Flask(__name__)   # parameter is the name of the module for a web app
                        # value __name__ contains the correct module name for the current file 
                        # it will contain the "__main__" value if the module is started directly,
                        # and another name if the module is connected

@app.route('/')  # Decorating the function - assigning a URL to it
def index():
    data = request.args.get('name', 'no data')
    conn = sqlite3.connect('Artistc.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM artists WHERE Name LIKE ?", (f"%{data}%",))
    result = cursor.fetchall()
    string_result = ', '.join([row[0] for row in result]) if result else 'no data'
    conn.close()
    """ The function returns the text of a document """
    return string_result

if __name__ == "__main__":
    # Starting the web server:
    app.run() 

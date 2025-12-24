""" The program uses flask and runs a web server. 
When requesting this server, it returns the contents of the index.html file
The file is processed as a template. It is not located! """
from flask import Flask, render_template

def index():
    """ the function handles the template index.html and returns the resulting document"""
    return render_template('index.html')

app = Flask(__name__) 

# creating a rule for URL '/': 
app.add_url_rule('/', 'index', index)

# Starting the web server:
app.run()
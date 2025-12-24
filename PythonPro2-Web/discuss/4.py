""" Passing information to the template: tags are ignored!
The formatting is specified in the template, the data should not contain information about the formatting.
Pay attention: CSS is not working all this time!
"""
from flask import Flask, render_template
import os

def index():
    """ the function handles the template index.html        and returns the resulting document"""
    return render_template('index1.html ', header="And if you try", text="<i>Italics?</i>")

folder = os.getcwd() # remembering the current working folder
# Creating a web application object:
app = Flask(__name__, template_folder=folder, static_folder=folder) # the first parameter is the module name
                            # the parameter named static_folder defines the name of the folder containing the static files
                            # the parameter named template_folder defines the name of the folder containing the templates

# creating a rule for URL '/': 
app.add_url_rule('/', 'index', index)

if __name__ == "__main__":
    # Starting the web server:
    app.run()

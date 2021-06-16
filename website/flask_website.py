# -*- coding: utf-8 -*-
"""
Created on Thu May 13 10:56:13 2021

@author: siaaa013
"""


from flask import Flask , redirect, url_for, render_template

app = Flask(__name__)
a = False

@app.route("/<name>")
def home(name):
    return render_template("index.html", content = name, r = 2) 

def unused():
    
    
    #@app.route("/<name>")
    #def user(name):
        #return f"hello {name}"
        
    
    #@app.route("/admin")
    #def admin(): 
        #return redirect(url_for("user", name ="Admin!"))
    pass


if __name__ == "__main__":
    app.run()
    
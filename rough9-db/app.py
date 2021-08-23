from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_sqlalchemy import SQLAlchemy, Model
from textwrap import wrap
from os import listdir
import requests
import json



app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = r'sqlite:///C:/Users/Sudharsan/Downloads/OfflineBanking_flask-master/OfflineBanking_flask-master/rough9-db/sec.db'
db = SQLAlchemy(app)

app.secret_key = 'sudhar'



class Persons(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(120),primary_key=True)


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        uname = request.form["uname"]


        login = Persons.query.filter_by(Name=uname).first()
        #login.Name
        #chek = login.one().Name

        if login is not None:

            print(login)

            return "Already there"
        else:
            print(login)
            return 'you can proced'
    return render_template("app.html")



if __name__ == "__main__":
    db.create_all()

    app.run(debug=True, port=5038)

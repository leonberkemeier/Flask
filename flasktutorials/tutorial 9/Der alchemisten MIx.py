from flask import Flask, render_template
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask (__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    location = db.Column(db.String(50))
    date_created =  db.Column(db.DateTime, default =datetime.now)

@app.route("/<name>/<location>")
def index(name, location):
    user = User(name=name,location=location)
    db.session.add(user)
    db.session.commit()

def home():
    return render_template("home9.html")

if __name__ == "__main__":
    app.run(debug=True)
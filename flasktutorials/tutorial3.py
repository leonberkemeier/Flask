from flask import Flask, redirect, url_for,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index3.html")

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/<name>")
def user(name): 
    return render_template("index3.html")
    
if __name__ == "__main__":
    app.run(debug=True)
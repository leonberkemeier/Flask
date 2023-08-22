from flask import Flask, redirect, url_for,render_template

app = Flask(__name__)
a= False

@app.route("/<name>")
def home(name):
    return render_template("index2.html", content = name, r="nice to see you again", )
    
if __name__ == "__main__":
    app.run()
from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/")
def homepage ():
    return "WELCOME TO THE JUNGLE <h1>HERO<h1>"

@app.route("/<name>")
def user(name):
    return "HELLO " + name

@app.route("/admin")
def admin():
    return redirect(url_for("homepage"))
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)



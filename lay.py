from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/")
def homepage ():
    return "WELCOME <h1>THIS IS A SIMPLE FLASK APP CREATED BY AYODEJI IHIMODU TO DEMONSTRATE HIS KNOWLEDGE OF DEVOPS, APP IS CURRENTLY BEING RUN USING A COMBINATION OF A DOCKER IMAGE, JENKINS, AZURE CONTAINER REGISTRIES AND AN AKS CLUSTER IN AZURE<h1>"

@app.route("/<name>")
def user(name):
    return "HELLO " + name

@app.route("/admin")
def admin():
    return redirect(url_for("homepage"))
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)



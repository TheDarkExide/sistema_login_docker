from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["POST"])
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():

    # Proceso de verificación de usuario

    return render_template("welcome.html")

@app.route("/register", methods=["POST"])
def register():

    # Recuperar datos y almacenar en base

    return render_template("register.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

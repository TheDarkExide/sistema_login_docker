from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def get_db():
    pass

@app.route("/", methods=["POST"])
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]

    conn = get_db()
    user = conn.execute("SELECT * FROM users WHERE email = ? AND password = ?",
                        (email, password)).fetchone()
    conn.close()

    if user:
        return render_template("home.html", nombre=user["nombre"])
    else:
        return redirect(url_for("home"))

@app.route("/register", methods=["POST"])
def register():

    name = request.form["user"]
    email = request.form["email"]
    password = request.form["password"]

    return redirect(url_for(home))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

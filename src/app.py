from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'mi_clave_secreta'

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    if email == "usuario@correo.com" and password == "1234":
        return "Login exitoso"
    else:
        flash("Correo o contraseña incorrectos")
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
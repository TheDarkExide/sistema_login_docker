from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2

app = Flask(__name__)
app.secret_key = "el_que_quiera_perder_su_tiempo"

DB_HOST = "db"      
DB_NAME = "bd_login"       
DB_USER = "postgres"       
DB_PASS = "root"

def get_db_conn():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    return conn

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]

    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
    user = cur.fetchone()
    cur.close()
    conn.close()

    if user:
        return render_template("home.html", nombre_usuario=user[1])
    else:
        flash("Usuario o contraseña incorrectos")
        return redirect(url_for("home"))

@app.route("/register", methods=["POST"])
def register():

    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]
    confirm = request.form["confirm"]

    if password != confirm:
        flash("Las contraseñas no coinciden")
        return redirect(url_for("home"))

    conn = get_db_conn()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO users (nombre, email, password) VALUES (%s, %s, %s)",
            (name, email, password)
        )
        conn.commit()
    except psycopg2.IntegrityError:
        conn.rollback()
        flash("Ese correo ya está registrado")
    finally:
        cur.close()
        conn.close()

    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

from functools import wraps
import sqlite3

from flask import (
    Flask,
    render_template,
    request,
    session,
    redirect
)

# ===================================
# App Configuration
# ===================================

app = Flask(__name__)
app.secret_key = "saud-secret-key"


# ===================================
# Authentication Decorator
# ===================================

def login_required(f):

    @wraps(f)
    def wrapper(*args, **kwargs):

        if "username" not in session:
            return redirect("/")

        return f(*args, **kwargs)

    return wrapper


# ===================================
# Routes
# ===================================

@app.route("/")
def home():

    return render_template("Login-Page.html")


@app.route("/home")
@login_required
def home_page():

    services = [
        "VPN Management",
        "LDAP Management",
        "DNS Management",
        "Jabber Management",
        "Server Management",
        "Statistics Management",
        "Log Management",

    ]

    return render_template(
        "Home-page.html",
        username=session.get("username"),
        services=services
    )


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "GET":
        return redirect("/")

    username = request.form["username"]
    password = request.form["password"]

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cursor.fetchone()

    conn.close()

    if user:

        session["username"] = username

        return render_template(
            "Login-Success.html",
            result=f"Welcome {username} 🎉"
        )

    return render_template(
        "Login-Page.html",
        result="Invalid Username or Password ❌"
    )

@app.route("/whoami")
@login_required
def whoami():

    conn = sqlite3.connect("users.db")

    cursor = conn.cursor()

    cursor.execute(
        "SELECT username, password FROM users WHERE username=?",
        (session["username"],)
    )

    user = cursor.fetchone()

    conn.close()

    return {
        "username": user[0],
        "password": user[1]
    }
@app.route("/logout")
@login_required
def logout():

    session.pop("username", None)

    return redirect("/")


# ===================================
# Run Application
# ===================================

if __name__ == "__main__":
    app.run()
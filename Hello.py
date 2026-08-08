from functools import wraps
from flask import Flask, render_template, request, session, redirect
import sqlite3

app = Flask(__name__)
app.secret_key = "saud-secret-key"

def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):

        if "username" not in session:
            return redirect("/")

        return f(*args, **kwargs)

    return wrapper
@app.route("/")
def home():
    return render_template("Login-Page.html")


@app.route("/home")
@login_required
def home_page():
    services = [
        "Create Incident",
        "Check Ticket Status",
        "Network Health Check",
        "Generate Report",
        "Contact Support"
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

    else:

        return render_template(
            "Login-Page.html",
            result="Invalid Username or Password ❌"
        )

@app.route("/logout")
def logout():

    session.pop("username", None)

    return redirect("/")

if __name__ == "__main__":
    app.run()
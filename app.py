import sqlite3
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("coffee_db.sqlite")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS coffees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            votes INTEGER DEFAULT 0
        )
    """)

    cursor.execute("SELECT COUNT(*) FROM coffees")

    if cursor.fetchone()[0] == 0:
        coffees = [
            "Espresso",
            "Cappuccino",
            "Latte",
            "Mocha",
            "Cold Brew"
        ]

        for coffee in coffees:
            cursor.execute(
                "INSERT INTO coffees (name) VALUES (?)",
                (coffee,)
            )

    conn.commit()
    conn.close()

init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/coffees", methods=["GET"])
def get_coffees():
    conn = sqlite3.connect("coffee_db.sqlite")
    cursor = conn.cursor()

    cursor.execute("SELECT name, votes FROM coffees")
    coffees = cursor.fetchall()

    conn.close()

    return jsonify([
        {"name": c[0], "votes": c[1]}
        for c in coffees
    ])

@app.route("/vote", methods=["POST"])
def vote():

    data = request.get_json()
    coffee_name = data.get("name")

    conn = sqlite3.connect("coffee_db.sqlite")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE coffees
        SET votes = votes + 1
        WHERE name = ?
    """, (coffee_name,))

    conn.commit()

    cursor.execute(
        "SELECT votes FROM coffees WHERE name=?",
        (coffee_name,)
    )

    votes = cursor.fetchone()[0]

    conn.close()

    return jsonify({
        "name": coffee_name,
        "votes": votes
    })

if __name__ == "__main__":
    app.run(debug=True)
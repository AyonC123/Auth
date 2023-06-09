from flask import Blueprint, request, jsonify
import sqlite3
import base64

views = Blueprint(__name__, "views")


@views.route("/signup", methods=["POST", "GET"])
def signUp():
    con = sqlite3.connect("example.db")
    cur = con.cursor()
    cur.execute(
        """CREATE TABLE IF NOT EXISTS signup (name text PRIMARY KEY, email text)"""
    )
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        cur.execute(
            """INSERT OR IGNORE INTO signup VALUES (?, ?)""", (name, email)
        )
        con.commit()
        return jsonify({"name": name, "email": email})
    else:
        data = []
        for row in con.execute("""SELECT * FROM signup"""):
            print(row[1])
            data.append({
                "name": row[0],
                "email": row[1]
            })
        return jsonify(data)

from flask import Blueprint, request, jsonify
import sqlite3

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
        cur.execute(f"""INSERT OR IGNORE INTO signup VALUES ({name}, {email})""")
        con.commit()
        return jsonify({"name": name, "email": email})
    else:
        for row in con.execute("""SELECT * FROM signup"""):
            print(row)
        return jsonify({})

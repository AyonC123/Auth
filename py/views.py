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
            f"""INSERT OR IGNORE INTO signup VALUES ({name}, {base64.b64encode(email.encode('ascii')).decode('ascii')})"""
        )
        con.commit()
        return jsonify({"name": name, "email": email})
    else:
        data = []
        for row in con.execute("""SELECT * FROM signup"""):
            data.append(
                {
                    "name": row["name"],
                    "email": base64.decode(row["email"].encode("ascii")).decode(
                        "ascii"
                    ),
                }
            )
        return jsonify(data)

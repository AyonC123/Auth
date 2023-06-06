from flask import Blueprint, request, jsonify

views = Blueprint(__name__, "views")

@views.route("/signup", methods=["POST", "GET"])
def signUp():
  if request.method == "POST":
    name = request.form["name"]
    email = request.form["email"]
    return jsonify({"name": name, "email": email})
  else:
    return jsonify({})
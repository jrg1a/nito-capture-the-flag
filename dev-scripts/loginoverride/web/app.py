from flask import Flask, request, make_response, render_template, send_from_directory
import hashlib

app = Flask(__name__, static_url_path='/static')

@app.route("/robots.txt")
def robots():
    return send_from_directory(app.static_folder, "robots.txt")

@app.route("/", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        creds = {{"admin": "{sha256('supersecret'.encode()).hexdigest()}"}}
        if username in creds:
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            if creds[username] == password_hash:
                return "Flag: NITO{{hash_bypass_master}}"
            else:
                message = "Access Denied"
        else:
            message = "Access Denied"
    return render_template("login.html", message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

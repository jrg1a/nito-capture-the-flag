from flask import Flask, request, make_response, render_template

import base64

app = Flask(__name__)

@app.route("/")
def index():
    user_cookie = request.cookies.get("user")
    
    # Hvis cookien ikke finnes, sett den til 'guest'
    if not user_cookie:
        encoded_guest = base64.b64encode("guest".encode()).decode()
        resp = make_response(render_template("index.html", user="guest"))
        resp.set_cookie("user", encoded_guest)
        return resp

    # Prøv å dekode cookien
    try:
        decoded = base64.b64decode(user_cookie.encode("ascii")).decode("utf-8")
    except Exception:
        decoded = "guest"

    if decoded == "admin":
        return "Flag: NITO{c00ki3s_4r3_p0w3rfu1}"

    # Returner som vanlig, men beholder eksisterende cookie
    resp = make_response(render_template("index.html", user=decoded))
    resp.set_cookie("user", user_cookie)  # Bare for å forsikre at den eksisterer
    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask, request, redirect, render_template, send_from_directory
import hashlib

app = Flask(__name__)

# Hardcoded password for demonstration purposes
# In a real application, you should store the hashed password in a database and retrieve it on login
password = "4e026537a7d32360c5a22b7cb2e7f61a" # "password" hashed with MD5

# Login page
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        entered_password = request.form.get("password")
        hashed_password = hashlib.md5(entered_password.encode()).hexdigest()
        res = redirect("/home")
        if (hashed_password == password):
            if ("visited" in request.cookies):
                print();
            else:
                res.set_cookie('visited', 'yes')
            return res
        else:
            return render_template("login.html", error="Incorrect password")
    return render_template("login.html")

# Welcome page
@app.route("/home")
def welcome():
    if ("visited" in request.cookies):
        return render_template("index.html")
    else:
        print("Verification has expired. Returning to login screen.")
        return redirect("/")

@app.route("/about")
def about():
    if ("visited" in request.cookies):
        return render_template("about.html")
    else:
        print("Verification has expired. Returning to login screen.")
        return redirect("/")

@app.route("/contact")
def contact():
    if ("visited" in request.cookies):
        return render_template("contact.html")
    else:
        print("Verification has expired. Returning to login screen.")
        return redirect("/")

@app.route("/Glass Family Photos Archive/<path:filename>")
def image(filename):
    if ("visited" in request.cookies):
        return send_from_directory("Glass Family Photos Archive", filename)
    else:
        print("Verification has expired. Returning to login screen.")
        return redirect("/")

@app.route("/styles/<path:style>")
def getstyle(style):
    return send_from_directory("styles", style)

@app.route("/<path:page>")
def getpage(page):
    if ("visited" in request.cookies):
        return render_template(page)
    else:
        print("Verification has expired. Returning to login screen.")
        return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
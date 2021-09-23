from app import app
from flask import redirect, render_template, request, session
import users
import places

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/mainpage")
        else:
            return render_template("error.html", message="Hups! Väärä tunnus tai salasana")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Hups! Salasanat eroavat")
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", message="Hups! Rekisteröinti epäonnistui")

@app.route("/mainpage", methods=["GET", "POST"])
def mainpage():
    return render_template("mainpage.html", places=places.get_all_places())
    
@app.route("/places/<int:place_id>")
def show_place(place_id):
    info = places.get_place_info(place_id)
    print(info)


    #reviews = places.get_reviews(place_id)

    return render_template("place.html", id=place_id, name=info[0], description=info[1])
                            #reviews=reviews)   

@app.route("/review")
def reviews():
    return render_template("error.html", message="Kiitos mielenkiinnosta. Tulossa pian!")                            
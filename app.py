import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask_paginate import Pagination
if os.path.exists("env.py"):
    import env

UPLOAD_FOLDER = '/workspace/ms3-recipedia/static/imgs/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

# create an instance of flask
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes)


# used minin project walkthrough for user authentication
@app.route("/register", methods=["GET", "POST"])
def register():
    # Check if a username exists
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("already a user")
            return redirect(url_for('register'))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into session
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if a user exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check hashed password
            if check_password_hash(
                existing_user['password'], request.form.get('password')):
                    session['user'] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(
                        url_for("profile", username=session["user"]))
            else:
                # password doesn't match
                flash("Incorrect Username and/or Password, Please try again")
                return redirect(url_for("login"))
        else:
            # username does not exist
            flash("Incorrect Username and/or Password, Please try again")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # get the session users username
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    recipes = mongo.db.recipes.find()

    if session["user"]:
        return render_template(
            "profile.html", username=username, recipes=recipes)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove the user from their session - logout
    flash("You have been logged out.")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["POST", "GET"])
def add_recipe():
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    categories = mongo.db.categories.find().sort(
        "category_name",1)
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        steps = request.form.getlist("steps")
        step_list = []
        for step in steps:
            step_list.append(step)
        ingredients = request.form.getlist("ingredients")
        ingredients_list = []
        for ingredient in ingredients:
            ingredients_list.append(ingredient)
        recipes = {
            "recipe_name": request.form.get("recipe_name"),
            "created_by": session["user"],
            "date": request.form.get("date"),
            "category": request.form.get("category"),
            "difficulty": request.form.get("difficulty"),
            "prep_time": request.form.get("recipe_name"),
            "servings": request.form.get("servings"),
            "cook_time": request.form.get("cook_time"),
            "img_upload": request.form.get("img_upload"),
            "steps": request.form.get("steps"),
            "ingredients": ingredients_list,
            "steps": step_list
        }
        mongo.db.recipes.insert_one(recipes)
        flash("Thanks")
        return redirect(url_for("get_recipes"))
    return render_template("add_recipe.html", username=username,
                           categories=categories)



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
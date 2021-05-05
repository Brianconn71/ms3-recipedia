import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from flask_paginate import Pagination, get_page_args
if os.path.exists("env.py"):
    import env


# create an instance of flask
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    # got help and advice on pagination from here
    # : https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page',
        offset_parameter='offset')
    per_page = 6
    offset = (page - 1) * 6
    total = mongo.db.recipes.find().count()
    recipes = list(mongo.db.recipes.find())
    recipes_paginated = recipes[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page,
                            total=total, css_framework='materializecss')
    return render_template("recipes.html", recipes=recipes_paginated,
                            page=page, per_page=per_page,
                            pagination=pagination)


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
    if request.method == 'POST':
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
            "prep_time": request.form.get("prep_time"),
            "servings": request.form.get("servings"),
            "cook_time": request.form.get("cook_time"),
            "img_upload": request.form.get("img_upload"),
            "ingredients": ingredients_list,
            "steps": step_list
        }
        mongo.db.recipes.insert_one(recipes)
        flash("Your recipe has been added to the database")
        return redirect(url_for("add_recipe"))
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_recipe.html", username=username,
                           categories=categories)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == 'POST':
        steps = request.form.getlist("steps")
        step_list = []
        for step in steps:
            step_list.append(step)
        ingredients = request.form.getlist("ingredients")
        ingredients_list = []
        for ingredient in ingredients:
            ingredients_list.append(ingredient)
        edit_recipes = {
            "recipe_name": request.form.get("recipe_name"),
            "created_by": session["user"],
            "date": request.form.get("date"),
            "category": request.form.get("category"),
            "difficulty": request.form.get("difficulty"),
            "prep_time": request.form.get("prep_time"),
            "servings": request.form.get("servings"),
            "cook_time": request.form.get("cook_time"),
            "img_upload": request.form.get("img_upload"),
            "ingredients": ingredients_list,
            "steps": step_list
        }
        mongo.db.recipes.update(
                                {"_id": ObjectId(recipe_id)}, edit_recipes)
        flash("Your recipe has been successfully updated")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_recipe.html", recipe=recipe,
                           categories=categories)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
    flash("Recipe has been deleted successfully")
    return redirect(url_for("get_recipes"))


@app.route("/get_categories")
def get_categories():
    categories = list(
        mongo.db.categories.find().sort("category_name", 1))
    return render_template("recipe_categories.html", categories=categories)


@app.route("/full_recipe/<recipe_id>")
def full_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)})
    return render_template("full_recipe.html", recipe=recipe)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
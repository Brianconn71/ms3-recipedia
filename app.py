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
    # https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9
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
                           page=page,
                           per_page=per_page,
                           pagination=pagination)


@app.route("/search", methods=["GET", "POST"])
def search():
    """
        This function uses the text index to search the DB
        based on the recipe name and what the user types into the searchbar.
    """
    search = request.form.get("search")
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page',
        offset_parameter='offset')
    per_page = 6
    offset = (page - 1) * 6
    total = mongo.db.recipes.find({"$text": {"$search": search}}).count()
    recipes = list(mongo.db.recipes.find({"$text": {"$search": search}}))
    recipes_paginated = recipes[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page,
                            total=total, css_framework='materializecss')
    if len(recipes) <= 0:
        flash(f"No recipes of {search} were found!")
    else:
        flash(f"Your search for {search} returned {len(recipes)} result(s)!")
    return render_template("recipes.html", recipes=recipes_paginated,
                           page=page, per_page=per_page,
                           pagination=pagination)


@app.route("/category_search/<id>")
def category_search(id):
    """
        This function searches for the recipes various categories in the Db.
        When the user then clicks on the filter button i.e "Breakfast"
        The breakfast recipes are loaded and paginated on the page
    """
    recipes = list(mongo.db.recipes.find({"category": id}))
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page',
        offset_parameter='offset')
    per_page = 6
    offset = (page - 1) * 6
    total = len(recipes)
    recipes_paginated = recipes[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page,
                            total=total, css_framework='materializecss')
    if len(recipes) <= 0:
        flash(f"No recipes of {id} were found!")
    else:
        flash(f"Your search for {id} returned {len(recipes)} result(s)!")
    return render_template("recipes.html", recipes=recipes_paginated,
                           page=page, per_page=per_page,
                           pagination=pagination)


# used CI project walkthrough for user authentication
@app.route("/register", methods=["GET", "POST"])
def register():
    """
        This function follows the CI walkthrought project of Task Manager,
        which allows users to register on the site
    """
    # Check if a username exists
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username is already taken")
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
    """
        This function follows the CI walkthrought project of Task Manager,
        which allows users to login to the site and land on their profile page
    """
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
                # if password doesn't match
                flash("Incorrect Username and/or Password, Please try again")
                return redirect(url_for("login"))
        else:
            # username does not exist
            flash("Incorrect Username and/or Password, Please try again")
            return redirect(url_for("login"))

    return render_template("login.html")


"""
    The below function displays a users profile
    with the recipes they have created along with
    recipes they have saved to there profile,
    I got help from many different Slack sources and from my mentor
    in making the below function along with help
    removing duplicates from a list here:
    https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/
"""


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # get the session users username
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    recipes = list(mongo.db.recipes.find({"created_by": session['user']}))
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page',
        offset_parameter='offset')
    per_page = 6
    offset = (page - 1) * 6
    total = len(recipes)
    recipes_paginated = recipes[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page,
                            total=total, css_framework='materializecss')
    recipes_saved = []
    recipe = []
    """
        Spent a long time stuck on this as not every user
        will have a saved recipe, the best way that I could get around the
        issues that kept arrising was to use try and except with a key error,
        its not very elegant but it does the job, additional info found here:
        https://stackoverflow.com/questions/45155991/try-except-error-exception-keyerror
    """
    if session['user']:
        try:
            """
            if session user is in session then try to find the saved_recipes
            key in the users Db, if not there then ignore trying to find it,
            and don't return the saved recipes section of profile page,
            if the user has a saved_recipes key in the users Db then return,
            the saved recipes from the array to display on the profile page.
            """
            saved_recipes = mongo.db.users.find_one(
                {"username": session["user"]})["saved_recipes"]
            if saved_recipes is not None:
                for rec in saved_recipes:
                    recipe = mongo.db.recipes.find_one({'_id': ObjectId(rec)})
                    recipes_saved.append(recipe)
                result = []
                for i in recipes_saved:
                    if i not in result:
                        result.append(i)
                return render_template(
                    "profile.html", username=username,
                    recipes=recipes_paginated, result=result,
                    page=page, per_page=per_page,
                    pagination=pagination)
            else:
                return render_template(
                    "profile.html", username=username,
                    recipes=recipes_paginated, page=page,
                    per_page=per_page, pagination=pagination)
        except KeyError:
            return render_template(
                "profile.html", username=username,
                recipes=recipes_paginated, page=page,
                per_page=per_page, pagination=pagination)
    else:
        return render_template('403.html')


@app.route("/logout")
def logout():
    """
        Taken and modified from the CI walkthrough project
    """
    # remove the user from their session - logout
    flash("You have been logged out.")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["POST", "GET"])
def add_recipe():
    """
        adding a recipe to the database guidance sought from CI Walkthrough.
    """
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
    """
        This function will edit a chosen recipe
    """
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
    """
        This function deletes a recipe from the recipes Db
    """
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe has been deleted successfully")
    return redirect(url_for("get_recipes"))


@app.route("/full_recipe/<recipe_id>")
def full_recipe(recipe_id):
    """
        This function will show a single recipe on a new page
        and display all info.
    """
    recipe = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)})
    return render_template("full_recipe.html", recipe=recipe)


@app.route("/get_categories")
def get_categories():
    """
        This Function will get all categories from the categories Db
    """
    categories = list(
        mongo.db.categories.find().sort("category_name", 1))
    return render_template("recipe_categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    """
        This function will add another category to the db
    """
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New recipe Category has been added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    """
        This function will edit a chosen category
    """
    if request.method == "POST":
        submit_category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update(
            {"_id": ObjectId(category_id)}, submit_category)
        flash("Categroy updated successfully")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    """
        This function will delete a chosen category from the Db
    """
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category has been deleted successfully")
    return redirect(url_for("get_categories"))


@app.route("/full_product/<product_id>")
def full_product(product_id):
    """
        This function will display a product on its own page
        and display all information
    """
    product = mongo.db.products.find_one(
        {"_id": ObjectId(product_id)})
    return render_template("full_product.html", product=product)


@app.route("/get_products")
def get_products():
    """
        This function will search the products Db and return all products
        in paginated format.
    """
    products = list(
        mongo.db.products.find().sort("product_name", 1))
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page',
        offset_parameter='offset')
    per_page = 6
    offset = (page - 1) * 6
    total = mongo.db.products.find().count()
    products_paginated = products[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page,
                            total=total, css_framework='materializecss')
    return render_template("products.html",
                           products=products_paginated,
                           page=page, per_page=per_page,
                           pagination=pagination)


@app.route("/add_product", methods=["GET", "POST"])
def add_product():
    """
        This function will add a product to the products Db
    """
    if request.method == "POST":
        product = {
            "product_name": request.form.get("product_name"),
            "product_type": request.form.get("product_type"),
            "product_description": request.form.get("product_description"),
            "product_img": request.form.get("product_img"),
            "user_rating": request.form.get("user_rating")
        }
        mongo.db.products.insert_one(product)
        flash("New product has been added")
        return redirect(url_for("get_products"))

    return render_template("add_product.html")


@app.route("/edit_product/<product_id>", methods=["GET", "POST"])
def edit_product(product_id):
    """
        This function will allow admin to edit a product
    """
    if request.method == "POST":
        update_product = {
            "product_name": request.form.get("product_name"),
            "product_type": request.form.get("product_type"),
            "product_description": request.form.get("product_description"),
            "product_img": request.form.get("product_img"),
            "user_rating": request.form.get("user_rating")
        }
        mongo.db.products.update(
            {"_id": ObjectId(product_id)}, update_product)
        flash("Product updated successfully")
        return redirect(url_for("get_products"))

    product = mongo.db.products.find_one({"_id": ObjectId(product_id)})
    return render_template("edit_products.html", product=product)


@app.route("/delete_product/<product_id>")
def delete_product(product_id):
    """
        This function will allow admin to delete a product
    """
    mongo.db.products.remove({"_id": ObjectId(product_id)})
    flash("Product has been deleted successfully")
    return redirect(url_for("get_products"))


@app.route("/product_search/<id>")
def product_search(id):
    """
        This function will search the products db for all product types,
        and return them based on which button a user chooses in paginated
        format.
    """
    products = list(mongo.db.products.find({"product_type": id}))
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page',
        offset_parameter='offset')
    per_page = 5
    offset = (page - 1) * 5
    total = len(products)
    products_paginated = products[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page,
                            total=total, css_framework='materializecss')
    if len(products) <= 0:
        flash(f"No product type of {id} were found in our database!")
    else:
        flash(f"Your search for {id} returned {len(products)} result(s)!")
    return render_template("products.html", products=products_paginated,
                           page=page, per_page=per_page,
                           pagination=pagination)


@app.route("/save_recipe/<recipe_id>", methods=["GET", "POST"])
def save_recipe(recipe_id):
    """
        This function will allow users to save a recipe to their profile,
        It will push the recipe id of the recipe to the saved_recipes
        key in the users db and store it in an array.
        also got some help on pushing to mongo here:
        https://docs.mongodb.com/manual/reference/operator/update/push/
    """
    mongo.db.users.find_one_and_update(
        {"username": session["user"].lower()},
        {"$push": {"saved_recipes": ObjectId(recipe_id)}})
    flash("Recipe saved to your profile!")
    return redirect(url_for("get_recipes"))


@app.route("/remove_recipe/<recipe_id>", methods=["GET", "POST"])
def remove_recipe(recipe_id):
    """
        This function will allow users to remove a saved recipe from their
        profile and remove it from the array in the users Db
    """
    mongo.db.users.find_one_and_update(
        {"username": session["user"].lower()},
        {"$pull": {"saved_recipes": ObjectId(recipe_id)}})
    flash("Saved recipe has been removed")
    return redirect(url_for("profile", username=session["user"]))


"""
    all error handler functions were found and guidance
    got from here:
    https://www.askpython.com/python-modules/flask/flask-error-handling
"""


@app.errorhandler(403)
def forbidden_error(error):
    return render_template('403.html'), 403


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(403)
def internal_server_error(error):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)

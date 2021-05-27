# Recipedia

![Mock-Up of the site](https://github.com/Brianconn71/ms3-recipedia/blob/master/static/imgs/recipedia-responsive-view.JPG)

This is my 3rd milestone project for the Code Institute Full-Stack developer programme. I have chosen to do my project based on a cooking recipe website.

I decided to take inspiration from both the code institute student's handbook and my own interests to make a website dedicated to hosting recipes. it will allow users to log in and add their own recipes to the website and save other users recipes to their own profile for easy access and viewing.

I have made use of CRUD functionality throughout this project in allowing users to login, logout and register on the website. I also allow users to add recipes to the database, view other recipes, edit their own recipes that they have added to the website and delete their own recipes. the "admin" user has all functionality to the site icluding, adding, updating and deleting new products to the site and new categories.

A live preview of my site can be found [here](http://ms3-recipedia.herokuapp.com/get_recipes)

# Table of Contents

* [UX](#ux)
    * [strategy](#strategy)
        * [user stories](#user)
        * [site goals](#site)
    * [scope](#scope)    
        * [features](#features)
        * [future features](#future)
    * [structure](#structure)
    * [skeleton](#skeleton)
    * [surface](#surface)
* [Technologies used](#tech)
* [Testing](#testing)
* [Deployment](#deployment)
* [credits](#credits)

# UX <a name="ux">

## Strategy <a name="strategy">

I created this project as a way for users that have an interest in cooking, recipes and sharing their own recipes have a place to come and do all of those things.
I wanted to implement a social element to the site too, which I believe was achieved through the ability to save other users recipes for easy viewing on a users profile page.
I also set up a "Recipedia Utensils" page which people can use to view any utensils and cookware that are highly rated and are recommended by Recipedia, It is also a great way to generate income for site owners too. 
Admin users, are the select few in charge of the site and get freedom to do whatever they want with recipes including edit and delete recipes from anyone that adds a recipe to the site. Admin users can also add, remove and edit recipe categories and add, remove and edit products which normal users can not do.
I gave admin users the power to add categories, products and edit recipes mainly for safety purposes and security reasons.


### Site goals <a name="site">

* I want the site to be easy to use and have consistent design and imagery.

* I want the site to be responsive on all screen sizes.

* I want a way to generate income for the site.

* I want the site to be a one stop shop for everything cooking related.

* I want the site to have seamless integration with the MongoDB database.

* I want the navigation to be easy to understand and intuitive.

* I want to allow users to create an account on the site.

* I want to have an account that has full control over everything on the site for security reasons.

* I want to be able to add recommeneded products and categories to the site but not allow regular users that ability.

### User Stories <a name="user">

* I want to find recipes quickly and easily

* I want to be able to filter the recipes based on the type of recipe I want e.g Breakfast, Lunch and Dinner

* I want to be able to easily login to the site.

* I want to be able to easily Register an account on the site.

* I want to be able to add my own recipes to the site.

* I want to be to search the site based on a specific keyword in the recipe title.

* I want to be able to edit and delete my own recipes.

* I want to be able to view other members recipes easily.

* I want to be able to save other recipes for easy access and viewing in my profile.

* I want to be able to delete saved recipes that I no longer have a use for from my profile.

* I want to be able to view recommended kitchen products and purchase the products.

* I want to be able to easily view every recipe I have added to the site and make changes without having to look through every recipe on the site.

## Scope <a name="scope">

### Features <a name="features">

Nav bar

* The nav bar contains the links for all other pages on the site. It makes navigation much easier and straightforward for the user.

* The Nav bar is mobile responsive and uses the materialize sidenav for smaller screen sizes to be responsive. The sidenave opens from the right of the page.

* The logo gets centered when the screen gets to mobile view and the nav items move to the sidenav and are viewable when the menu icon is clicked.

Footer

* The footer contains the copyright and links to social media channels. These links will open on separate pages.

* The footer is mobile responsive and will change depending on screen size.

* The social media links have a .3s second transition and the color of the icons will change to the primary color of that particular social media channel

Recipes (Home) page

* Heading makes it clear to the user what it is that the site owner wants them to do on the site.

* Navigation bar again makes it easy for the user to get around the site and makes the links obvious and easy to see.

* Search bar allows users to find a recipe in the database based on the recipe name and will display relevant recipes below the search container, results will be displayed in paginated format with a max of six recipes per page

* Buttons (links) allow a user to filter the recipes in the database based on the type of recipe they wish to search for e.g Breakfast, results will be displayed in paginated format with a max of six recipes per page

* Heading and paragraphs below the filter buttons provide ease of use and navigation to the user and allows new users to click on register to create their own account and current users can click login to login to their profile.

* Latest recipes section then shows all the recipes in the database in paginated format with six recipes displayed per page, these recipes are automatically generated using the jinja for loop to display the recipes in the mongoDb.

Register page

* The register page will allow a user to create an account with the site and utilize all the offerings of the site such as add a recipe and save a recipe.

* The register container is mobile responsive and will change depending on the screen size.

* The python code will test the data input into the form by the user to make sure all data is correct and that the username is viable.

* To register a user will need to come up with a username and a password, the password field is stored as a hash in the mongoDb. There is a min and max input attribute that a user must satisfy along with a pattern of applicable characters, if a user hovers over the input fields more information is then given as to what is applicable for that input field.

* The fields are validated using materialize css classes.

* When the user successfully registers, they are put into session and redirected to their new profile page.

* Underneath the form, is a paragraph of information for users and a link for current users to login to their account, by clicking on this the user is then redirected to the login page.

Login page

* The Login page will allow a user to login to their accouint with the correct credentialsand utilize all the offerings of the site such as add a recipe and save a recipe. They will be redirected to their profile page.

* The login container is mobile responsive and will change depending on the screen size.

* The python code will test the data input into the form by the user to make sure that the username exists and that they are using a correct password.

* To Login a user will need to enter the correct account credentials for their account. If a user enters a wrong username or password a message will display at the top of the page informing them that they have entered an incorrect username or password and they will have to try again.

* The fields are validated using materialize css classes.

* When the user successfully enters the correct information, they will be put into session and redirected to their profile page.

* Underneath the form, is a paragraph of information for users and a link for current users to register an account, by clicking on this the user is then redirected to the register page.

Recipedia Utensils

* Heading makes it clear to the user what it is that the site owner wants them to do on the site.

* Filter buttons when clicked allow a user to filter the database and return in paginated form the results from that filter.

* After the user clicks on one of the buttons to filter the database, a flash message appears at the top of the page to inform the user the results of their filter based on the button they clicked.

* pagination info and pagination links will inform the user how many records were in their search and how many pages of search results their are.

* The products will then be shown that are in the database in paginated format with six products displayed per page, these products are automatically generated using the jinja for loop to display the products in the mongoDb.

* The products will display on cards, these cards will contain a button which a user can click to see the full product information and description on a page of its own, the cards will also contain a buy now link which a user can click on to attempt to buy the product, There will also be a rating out of five for each product which will provide the user with insight into how good or bad an item is depending on the site owners or "admins" views, Finally, the cards will also display edit and delete buttons only to the admin user as the admin user is the only person who can add products to the site for security reasons.

Profile page

* once logged in the user will be greeted with a welcome message.

* Heading makes it clear to the user that they are on their profile page. A small introductory paragraph will be displayed below the main heading on the page.

* the next section on the page will display all the recipes that a user has saved (This feature will only appear if the user has actually saved recipes and won't appear straight away) This section will allow users to see recipes that they have saved for easy viewing, It will include buttons to see the full recipe on its own page and edit and delete buttons but these will only be available to the user who created the recipe.

* On the saved recipes cards there will be an unsave button which when clicked will remove the recipe from the saved_recipes field in the users table in the backend, the recipe will then be removed from the users profile and a message will appear at the top of the page telling the user that the recipe has been removed from their profile.

* Below this section will be a section to show the user all the recipes that they have added to the database. If the user has no recipes in the database a paragraph will show explaining to the user that they have no recipes in the database and will encourage them to add a recipe by means of a link that will take the user to the add recipe page.

* The recipes that a user has added to the database will appear in paginated format.

Edit Button

* Edit button is pretty self-explanatory, if a user clicks on the edit button it will allow them top make changes to their recipes and submit the new changes to the database. when submitted a message will display ot the user telling them that the recipe has been updated.

* Admin users will be able to edit all recipes, products and product categories.

Delete Button

* Delete button will be available to users to delete any recipes that they have added to the database.

* A delete confirmation modal will pop up on the screen to confirm with the user that they wish to delete will be deleted from the database should they choose confirm, if they choose cancel then they will be taken back to the recipes page.

* Admin users will have full delete capabilites over recipes, products and categories

* A delete confirmation will pop up whenever a delete was successfully executed.

Add recipe page

* Heading makes it clear to the user what it is that the site owner wants them to do.

* The add recipe page has a form which a user can use to input data for a recipe that they wish to add to the database.

* Jquery has been added to make the form dynamic and allow users to  add more ingredients and steps to the recipe, these will then get added to an array in the database. They can also remove a step or ingredient by clicking on the remove button below that input field. Loop index was also used here to ensure each label has the correct number when adding and removing.

* when a user has entered the correct data into each input field and the click on the add recipe button then the python code in the backend will add the recipe to the database.

Edit a recipe page

* When a user clicks on the edit button, it takes them to a page with a form that is pre-filled with the data of the recipe that they selected to edit. 

* The user can change any data that they wish to change here. when they click on the edit button at the bottom of the form then the changes will be made on the recipe with that recipe id in the database.

* The user can also cancel any changes by clicking the red x button at the bottom of the form. This will return them to the recipes home page.

* After the user clicks on edit button, the python code in the backend will add the updated code to the database.

Error pages

* All error pages (404, 403, 500) will display a very similar message to the user.

* They will have a header informing the user on what the error they have encountered is and a paragraph underneath the header explaining to the user how they can get back on the right track and return to the homepage. A link will be visible and when a user clicks on the link they will return to the homepage.

* All Error pages will respond to changes in screen size.

Recipe categories page (Admin users only)

* Heading makes it clear to the user what it is that the site owner wants them to do.

* This page will display to admin users all of the recipe categories currently listed in the categories Db. 

* The page will be responsive and respond accordingly to changes in screen size.

* The admin user will be able to add a new category, delete a category and edit a category name from this page.

* if the admin users clicks on the blue edit button they will be taken to an edit category page, if a user clicks on the red delete button a delete confirmation modal will pop up allowing the user to confirm the deletion of the category from the database or cancel the deletion. if the user clicks on the brown add category button then the user will be redirected to a page allowing them to add a new category to the database.

* Data (category names) are dynamically generated and displayed or removed from the page.

Edit a Recipe category page (Admin users only)

* Heading makes it clear to the user what it is that the site owner wants them to do.

* This page displays a form to the user with the prefilled category name of the category they have chosen to edit.

* Any changes made here will be added to the category db with that specific category id via the backend python code.

* The page also displays a edit button which when the user has made the required changes will submit the data to the backend which pushes it to the database. The user will then be redirected back to the categories page and notified that the changes were updated successfully.

* There is also a cancel changes button which when selected will cancel the new changes being made to the category and redirect thge user pack to the categories page.

Add Product Page (Admin Users Only)

* Heading makes it clear to the user what it is that the site owner wants them to do.

* This page displays a form to the user which when filled in with data will add a new product to the products Db.

* The page allows a user to enter a product name, description, type, image and rating out of 5, all fields are validated before the form is allowed to be sent and the user is then redirected back to the products page.

* When a user has entered all of the correct data into the input fields and clicks on the brown add product button at the bottom of the form, the data will be added to the Products Db via the backend Python Code.

Edit Product Page (Admin Users Only)

* Heading makes it clear to the user what it is that the site owner wants them to do.

* This page displays a form to the user with the prefilled product information of the product the user has chosen to edit.

* Any changes made here will be added to the products db with that specific product id via the backend python code.

* The page also displays a edit button which when the user has made the required changes will submit the data to the backend which pushes it to the database. The user will then be redirected back to the products page and notified that the changes were updated successfully.

* There is also a cancel changes button which when selected will cancel the new changes being made to the product and redirect the user back to the products page.

* This page like all other pages is fully mobile responsive.

Full Product Page

* This page will display the full information and description of a product on its own page.

* It will display on a card with all of the information that was available to see on the products page with the added inclusion of the full product description.

* The page will also display edit and delete buttons to the admin user only to edit or delete the product from the database.

Full Recipe Page

* This page will display the full information and description of a Recipe on its own page.

* It will display on a card with all of the information that was available to see on the recipes page with the added inclusion of all of the ingredients, steps, cook and prep time etc.

* The page will also display edit and delete buttons to the admin user and the user who created the recipe to allow for changes or the deletion of the recipe from the database.

### Future Features <a name="future">

* A "share to Social Media" button to integrate social media sharing of recipes.

* Nutritional information of recipes e.g. protein, fat, Kcals - would be very beneficial to health conscious users.

* Admin functionality to delete users - problematic users who cause issues may need to be deleted and this would be a good way to go about it.

* A rating system to allow users to filter based on rating from kigh to low, other filters could be beneficial too in terms of easy recipes, pricing of ingredients etc.

* upload files as images and not rely solely on urls for image uploads- I had planned to do this for this current project but I found it a bit too complicated.

## structure <a name="structure">

The structure of the site will remain consistent throughout the site. The same background image will be the background to each page on the site. Navigation will remain consistent throughout, Links and buttons will allow for easier access throughout the site. 

## skeleton <a name="skeleton">

### Wireframes

[Click here](https://github.com/Brianconn71/ms3-recipedia/blob/master/static/imgs/wireframes/recipedia%20wireframes.pdf) to view my Wireframes for this project.

![Recipedia Wireframes](https://github.com/Brianconn71/ms3-recipedia/blob/master/static/imgs/readme_imgs/recipedia-wireframes.png)

### Database design

The backend python code adds entries into the databases. Below are images of entries into the database.

#### Recipes Database

Users may add recipes to the database and edit recipes that they have previously created. The backend python code will then insert the data into the mongodb table labelled recipes. I use Jinja templating to display recipes on the site. Below is an example of an entry into the database.

![Recipe database entry](https://github.com/Brianconn71/ms3-recipedia/blob/master/static/imgs/readme_imgs/recipes-db.JPG)

#### Users Database

The users database stores the users name and password that they used to register for the site. The password is salted in the database. The users database will also store an array of recipe ids for recipes the user has saved to siaplay on their profile. This field will not be added to the database until a user saves their first recipe and then the backend python code will push the new field to the correct user id in the database. Below are two images, the first image is a user who has no saved recipes and the second is for a user who has a saved recipe.

![User with no saved recipes](https://github.com/Brianconn71/ms3-recipedia/blob/master/static/imgs/readme_imgs/user-db-without%20array.JPG)

![User with saved recipes](https://github.com/Brianconn71/ms3-recipedia/blob/master/static/imgs/readme_imgs/users-db-with%20array.JPG)

#### Categories Database

Categories database stores the different types of categories available for a user to select when adding a recipe to the database. Only Admin users can add, edit or delete categories in the database. Below is an image of a category entry into the database

![Category database entry](https://github.com/Brianconn71/ms3-recipedia/blob/master/static/imgs/readme_imgs/categories-db.JPG)

#### Products Database

Products database provides the content to the products page on the site. Admin users are the only ones that can add, update or delete products on the site in the database. Below is an  image of an entry in the products database.

![Products database entry](https://github.com/Brianconn71/ms3-recipedia/blob/master/static/imgs/readme_imgs/products%20-db.JPG)

## Surface <a name="surface">

There are many differences between the wireframes and the actual site. The biggest difference is the background image which I initially liked but as the project developed I felt that the image used in the wireframes was not conveying the message of the site so I changed it to an image displaying a multitude of vegetables.

I wanted to have a bright colored and easy to read and use site. Keeping consistency thoughout the project and maintaining consistent coloring on the buttons was important too. I had initally used a different buttons color early into the site but as the project developed I felt it was clashing with the other colors and images on the site so that got changed too.

I started to wander off from the wireframes after a while in the poroject, I just felt that consistency was the most important thing and I wanted coloring, pages buttons etc to be easy to look at and enjoyable.

### colors

The colors used in this project were found using [Paletton](https://paletton.com/). I spent a great deal of time searching for the right color scheme. Initially, I had a different color scheme in mnd but I didn't like it so I changed it using similar colors on paletton. Below are the colors that were used throughout the project.
* --text-white: #feffde - this is the text color which remains consistent throughout the site
* --pale-green: #bdd2b6 - used as sidenav background color.
* --darker-green: #a2b29f used as the background color of the delete modal
* --darkest-green: #798777 - the color of the cards for recipes and products.
* --button-color: #7B6668 - the color of the submit and search buttons
* --gold-rating: #ffd700 - the color of the thums up rating icons
* --bright-green: #55b113 - the color of the see description and see recipe button
* --red-color: #910000 - the color of the selete and cancel buttons
* --blue-color: #187bcd the color of the edit buttons
* #3b5998 - Facebook icon hover color
* #E1306C - Instagram icon hover color
* #1DA1F2 - twitter icon hover color
* #FF9900 - amazon icon hover color

### Images

Images are credited below in the media section.

### Fonts

Two fonts were used in the making of the site. The main-heading, logo font used on the site was Ubuntu and the paragraph, sub-heading text used was Oxygen. The default font is sans-serif.

These fonts complement each other very well and have easy readibility which is key for visitors to my site. The compatibility of the fonts on my site was found using google fonts.

## Technologies Used <a name="tech">

* [Heroku](https://heroku.com)
    * Heroku was used to host and deploy my project

* [HTML](https://html.com)
    * HTML was used to structure my project.

* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
    * CSS was used to style my project.

* [JavaScript](https://www.javascript.com)
    * JavaScript was used to add logic and functionality to my site.

* [jQuery](https://jquery.com/)
    * jQuery was used in my project on the following parts:
    Mobie side-Nav, delete confirmation Modal, for verification of the select form elements, datepicker on the forms, I also used jQuery for the add ingredient and add step buttons and remove buttons to add/remove ingredients and steps.

* [Python](https://python.org)
    * My project uses Python for the backend logic of the website and to run the website on Heroku. The following Python modules are used in my project:
        * click==7.1.2 dnspython==2.1.0 Flask==1.1.2 flask-paginate==0.8.1 Flask-PyMongo==2.3.0 itsdangerous==1.1.0 pymongo==3.11.3 Werkzeug==1.0.1

* [Flask-Paginate](https://flask-paginate.readthedocs.io/en/master/)
    * Flask-Paginate was used in my project to paginate the recipes, products and profile page to account for recipes and products.

* [MongoDB](https://www.mongodb.com/1)
    * Mongo Db was used to create the database collection behind this project

* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
    * Flask was the web app framework used in this project

* [GitHub](https://github.com)
    * Github was used to host and store the sourcfe code of the project

* [Gitpod](https://gitpod.io)
    * Gitpod was the IDE that I used to create the site and push the changes to Github.

* [Git](https://git-scm.com/)
    * Git is the version control software used on the site. it was used to add, commit and push the code changes to github.

* [Figma](https://www.figma.com)
    * Figma was used to create the wireframes of the site.

* [Font Awesome](https://fontawesome.com)
    * Font Awesome was used to source and find the icons used on the site.

* [Favicon](https://favicon.io)
    * Favicon was used to create and add a favicon to the site.

* [Google Fonts](https://fonts.google.com)
    * The two fonts that I used on the site, Ubuntu and Oxygen, were found using google fonts.

* [Paletton](https://paletton.com)
    * Paletton was used to source the colors that were used on the site.

* [Materialize](https://materializecss.com/)
    * Materialize was used to add html/css components to the site and to make the site more visually appealing to the user.

* [Canva](https://canva.com)
    * Canva was used to create the favicon design for the site.

* [Google Chrome Dev Tools](https://www.google.com/chrome/dev/)
    * Google chrome tools were used for debugging purposes and to test different css styles and layouts of features.

* [W3](https://www.weschools.com)
    * W3 Schools was used to troubleshoot issues regarding html css and python throughout the course of thye project.

* [Autoprefixer](https://autoprefixer.github.io)
    * Autoprefixer was used to parse my css file and add the vendor prefixes.

* [TingPNG](https://tinypng.com)
    * TinyPNG was used to reduce the size of the background image of the site.

* [Techsini](https://techsini.com/multi-mockup/)
    * Techsini is a mockup generator and It was used to get the mock up image of the site in the Readme.

## Testing <a name="testing">

The testing section can be found [here](https://github.com/Brianconn71/ms3-recipedia/blob/master/testing.md)

## Deployment <a name="deployment">

This project was deployed on [Heroku](https://heroku.com).

I created this project using the Code Institute Gitpod Full Template. I created a new repository and used then clicked the "use this template" and created my coding environment on gitpod.

To account for version control throughout the project, I used the below commands in the termional on gitpod.

* git add -A - This was the command that I used to add all relevant changes to the staging area.

* git commit -m "commit message"- This was the command that I used to commit the changes that I made to the repository

* git push - This was the command I used to push all of the changes that I hyad commited previously to the Github repo.

### Deployment to heroku

To enable deployment to heroku, you will need a requirements.txt file and a Procfile to inform Heroku on the dependencies necessary to run the project in heroku.

To make a requirements.txt file then type the following command into the terminal window of the IDE that you are using: `pip3 freeze --local > requirements.txt`

To make a Procile then type the following command into the terminal window of the IDE that you are using: `echo web: python run.py > Procfile`

Now follow the below steps below to deploy to Heroku.

1. go to [Heroku](https://heroku.com).

2. Login to personal account.

3. click on the "New" button.

4. Select "create new app"

5. Select your nearest region (America or Europe)

Now, We need to connect the Github repository to our app on Heroku.

1. Click on the Deploy tab on the dashboard.

2. In the deployment method section, select GitHub.

3. You will then see a prompt to find the GitHub repository to connect too.

4. Enter the name of the repository for the project and search.

5. When it finds the required repository, click on the connect button.

Now, we need to include the environment variables.

1. Click on the settings tab on the dashboard.

2. Click on Reveal Config Vars button and then add the following information.
    1. key: IP, Value: 0.0.0.0
    2. key: PORT, Value: 5000
    3. key: MONGO_DBNAME, value: (Name of the database you are connecting too.)
    4. key: MONGO_URI, value: (The Mongo Uri can be found in MongoDb by going to clusters then clicking on connect and connect to your application and then changing the password and the dbname to what you initially set up)
    5. key: SECRET_KEY, value: (A custom secret key of your own choosing which is used to keep client-side sessions secure)

Now, We need to go back to the Deploy tab again to enable the automatic deployment feature.

1. Click on the  Deploy tab.

2. In the automatic deployment section, choose the branch you want to deploy from the GitHub repository and finally, click on the Enable Automatic deploy button.

### Run Locally

This project will not run locally without the database connections we set up with Heroku unless you set up an env.py file in your local IDE. This env.py file is needed to configure the following connections IP, PORT, MONGO_URI, MONGO_DBNAME AND SECRET_KEY. You must use the same connection details that you used in the deployment tab on Heroku in order for the connections to work. These details are private to the user and are not disclosed for security reasons. 

GitHub ignores this env.py file and does not show it in your repository due security issues.

1. Create an account or login to your [GitHub](https://github.com) account

2. Navigate to the GitHub [repository](https://github.com/Brianconn71/ms3-recipedia) of this project.

3. Click on the code drop-down menu

4. Download the ZIP file, unpackage the file locally and open with the ide of your choice OR Copy the URL from the HTTPS box.

5. Open an IDE locally of your choice and then open a terminal window in the IDE.

6. use `git clone` followed by the URL you copied from the repository in GitHub as a command in the terminal.

7. A clone of the project will now be available locally.

8. to get the project to work correctly you will then need to install the required packages. This can be achieved by running the following command in the terminal window: `pip install -r requirements.txt`

### Fork the project

1. Create an account or login to your [GitHub](https://github.com) account.

2. Navigate to the GitHub [repository](https://github.com/Brianconn71/ms3-recipedia) that you want to fork.

3. On the top right of the page, you will see a button labelled "Fork", Click this button.

4. By clicking the Fork button, a complete duplicate of the project will now be available in your GitHub repository.


## Credits <a name="credits">

### Content

* The idea for my project was a direct result of inspiration taken from the code institute student handbook which listed potential ideas for projects and as a result of my own passion for cooking. I wanted to make a site to appeal to users of all ages and make it easy for busy people to find recipes to suit their needs.

* The products listed on the site and their relevant images are all taken from [Nisbets.ie](https://www.nisbets.ie/), the products used in the project are credited below in the media section.

* The recipes listed on the site and their relevant images are all taken from [BBCGoodFood](https://www.bbcgoodfood.com/), which was found by means of a google search, the recipes used in the project are credited below in the media section.

* [Materialize](https://materializecss.com/) was used for html/css components to make the site more visually appealing to the user.

* Some of the backend Python code was taken and modified to suit the needs of my project from the walkthrough task manager project.

### Media

* Product images and descriptions:
    * Hygiplas Colour Coded Chefs Knife Set with Wallet [image](https://media.nisbets.com/asset/core/prodimage/largezoom/s088_group.jpg) [description](https://www.nisbets.ie/hygiplas-colour-coded-chefs-knife-set-with-wallet/s088)
    * Vogue Catering Tongs 10" [image](https://media.nisbets.com/asset/core/prodimage/largezoom/j608_vogue-catering-tongs.jpg) [description](https://www.nisbets.ie/vogue-catering-tongs-10in/j608)
    * Vogue Round Cast Iron Skillet Pan 255mm [image](https://media.nisbets.com/asset/core/prodimage/largezoom/m655_roundskillet1.jpg) [description](https://www.nisbets.ie/vogue-round-cast-iron-skillet-pan-255mm/m655)
    * Schneider Aluminium Baking Tray [image](https://media.nisbets.com/asset/core/prodimage/largezoom/228602.jpg) [description](https://www.nisbets.ie/schneider-aluminium-baking-tray/p_gt145)
    * Vogue 6 Piece Soft Grip Knife Set [image](https://media.nisbets.com/asset/core/prodimage/largezoom/s725_softgrip_6piece.jpg) [description](https://www.nisbets.ie/vogue-6-piece-soft-grip-knife-set/s725)
    * Hygiplas Colour Coded Chopping Mats Set [image](https://media.nisbets.com/asset/core/prodimage/largezoom/cp521_group.jpg) [description](https://www.nisbets.ie/hygiplas-colour-coded-chopping-mats-set/p_cp520)
    * Vogue Stainless Steel Colander 9" [image](https://media.nisbets.com/asset/core/prodimage/largezoom/k331-colander.jpg) [description](https://www.nisbets.ie/vogue-stainless-steel-colander-9in/k331)
    *  Vogue Orange Pate Terrine Mould 1.7Ltr [image](https://media.nisbets.com/asset/core/prodimage/largezoom/w456_pateterrineorange1.jpg) [description](https://www.nisbets.ie/vogue-orange-pate-terrine-mould-1700ml/w456)
    * Vogue Stainless Steel Saucepan 900ml [image](https://media.nisbets.com/asset/core/prodimage/largezoom/m922_saucepan1new.jp) [description](https://www.nisbets.ie/vogue-stainless-steel-saucepan-900ml/m922)
    * Vogue Stainless Steel Saucepan 3Ltr [image](https://media.nisbets.com/asset/core/prodimage/largezoom/230677.jpg) [description](https://www.nisbets.ie/vogue-stainless-steel-saucepan-3ltr/m944)
    * Vogue Stainless Steel Saucepan 8Ltr [image](https://media.nisbets.com/asset/core/prodimage/largezoom/230677.jpg) [description](https://www.nisbets.ie/vogue-stainless-steel-saucepan-8ltr/m946)

* Recipe images and descriptions:
    * Chorizo & mozzarella gnocchi bake [image](https://images.immediate.co.uk/production/volatile/sites/30/2020/08/gnocchi-1d16725.jpg?quality=90&webp=true&resize=300,272) [description](https://www.bbcgoodfood.com/recipes/chorizo-mozzarella-gnocchi-bake)
    * Halloumi Burgers [image](https://images.immediate.co.uk/production/volatile/sites/30/2020/08/halloumi-burgers-cb38d14.jpg?quality=90&webp=true&resize=300,272) [description](https://www.bbcgoodfood.com/recipes/halloumi-burgers)
    * Hearty lentil one pot [image](https://images.immediate.co.uk/production/volatile/sites/30/2020/08/hearty-lentil-one-pot-440-400-20ecfad.jpg?quality=90&webp=true&resize=300,272) [description](https://www.bbcgoodfood.com/recipes/hearty-lentil-one-pot)
    * Sticky Chinese chicken traybake [image](https://images.immediate.co.uk/production/volatile/sites/30/2020/08/sticky-chinese-chicken-traybake-f28c3b7.jpg?quality=90&webp=true&resize=300,272) [description](https://www.bbcgoodfood.com/recipes/sticky-chinese-chicken-traybake)
    * Creamy salmon, leek & potato traybake [image](https://images.immediate.co.uk/production/volatile/sites/30/2020/08/creamy-salmon-leek-potato-traybake-367b3ff.jpg?quality=90&webp=true&resize=300,272) [description](https://www.bbcgoodfood.com/recipes/creamy-salmon-leek-potato-traybake)
    * Chicken & bean enchiladas [image](https://images.immediate.co.uk/production/volatile/sites/30/2020/08/chickenbean-enchiladas-1044331.jpg?quality=90&webp=true&resize=300,272) [description](https://www.bbcgoodfood.com/recipes/chicken-bean-enchiladas)
    * Quick chicken hummus bowl [image](https://images.immediate.co.uk/production/volatile/sites/30/2020/08/quick-chicken-and-hummus-bowl-3863168.jpg?quality=90&webp=true&resize=300,272) [description](https://www.bbcgoodfood.com/recipes/quick-chicken-hummus-bowl)
    * Orzo & tomato soup [image](https://images.immediate.co.uk/production/volatile/sites/30/2020/08/tomato-and-orzo-soup-47fe2e7.jpg?quality=90&webp=true&resize=300,272) [description](https://www.bbcgoodfood.com/recipes/orzo-tomato-soup)
    * Chipotle chicken & slaw [image](https://images.immediate.co.uk/production/volatile/sites/30/2020/08/hot-wings-and-slaw-1903ce0.jpg?quality=90&webp=true&resize=300,272) [description](https://www.bbcgoodfood.com/recipes/chipotle-chicken-slaw)
    * Singapore sling [image](https://images.immediate.co.uk/production/volatile/sites/30/2020/08/singapore-sling-37315fa.jpg?quality=90&webp=true&resize=300,272) [description](https://www.bbcgoodfood.com/recipes/singapore-sling)
    * Chicken skewers with tzatziki [image](https://images.immediate.co.uk/production/volatile/sites/30/2020/08/chicken-skewers-with-tzatziki-f4698fa.jpg?quality=90&webp=true&resize=300,272) [description](https://www.bbcgoodfood.com/recipes/chicken-skewers-tzatziki)
    * Minty griddled chicken & peach salad [image](https://images.immediate.co.uk/production/volatile/sites/30/2020/08/minty-griddled-chicken-peach-salad-2-440-400-9da5092.jpg?quality=90&webp=true&resize=300,272) [description](https://www.bbcgoodfood.com/recipes/minty-griddled-chicken-peach-salad)
    * Toffee apple turnover puff pie [image](https://images.immediate.co.uk/production/volatile/sites/30/2021/03/Toffee-apple-turnover-puff-pie-4fd08c3.jpg?quality=90&webp=true&resize=300,272) [description](https://www.bbcgoodfood.com/recipes/toffee-apple-turnover-puff-pie)
    * Pepper steak with noodles [image](https://images.immediate.co.uk/production/volatile/sites/30/2021/03/Pepper-steak-with-noodles-d582f5c.jpg?quality=90&webp=true&resize=300,272) [description](https://www.bbcgoodfood.com/recipes/pepper-steak-with-noodles)
    * Coconut & squash dhansak [image](https://images.immediate.co.uk/production/volatile/sites/30/2020/08/coconut-squash-dhansak-a3a9133.jpg?quality=90&webp=true&resize=300,272) [description](https://www.bbcgoodfood.com/recipes/coconut-squash-dhansak)
    * Thai fried prawn & pineapple rice [image](https://images.immediate.co.uk/production/volatile/sites/30/2020/08/thai-aea8468.jpg?quality=90&webp=true&resize=300,272) [description](https://www.bbcgoodfood.com/recipes/thai-fried-prawn-pineapple-rice)
    * Sweet potato & chicken curry [image](https://images.immediate.co.uk/production/volatile/sites/30/2020/08/recipe-image-legacy-id-265673_11-439042b.jpg?quality=90&webp=true&resize=300,272) [description](https://www.bbcgoodfood.com/recipes/sweet-potato-chicken-curry)
    * Aperol spritz [image](https://images.immediate.co.uk/production/volatile/sites/30/2020/08/aperol-spritz-0e58f7b.jpg?quality=90&webp=true&resize=300,272) [description](https://www.bbcgoodfood.com/recipes/aperol-spritz)
    * Two-minute breakfast smoothie [image](https://images.immediate.co.uk/production/volatile/sites/30/2020/08/two-minute-breakfast-smoothie-4a4722d.jpg?quality=90&webp=true&resize=375,341) [description](https://www.bbcgoodfood.com/recipes/two-minute-breakfast-smoothie)
    * Breakfast egg wraps [image](https://images.immediate.co.uk/production/volatile/sites/30/2020/05/breakfast-egg-wraps-c0880fe.jpg?quality=90&webp=true&resize=375,341) [description](https://www.bbcgoodfood.com/recipes/breakfast-egg-wraps)
    * Frappe [image]() [description]()

* Background image for the site [here](https://images.unsplash.com/photo-1597362925123-77861d3fbac7?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80)

### Code Snippets

* I used Pagination in my project which I got help and guidance from using this [GitHub](https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9) project, I also used the documentation around [flask-paginate](https://flask-paginate.readthedocs.io/en/master/) to help with its functionality and getting it set up in my project.

* I used the following [webpage](https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/) to help to only show unique recipes to the user in their profile from the list of recipes they have saved.

* Ran into some errors on my profile page functionality, an answer was found with [try and except](https://stackoverflow.com/questions/45155991/try-except-error-exception-keyerror)

* Used the following [Documentation](https://www.askpython.com/python-modules/flask/flask-error-handling) to set up error handlers in the app.py file.

* Validation of Select Form elements using Javascript in the script.js file was taken from the CI Walkthrough Task Manager Project.

* I used the following [link](https://stackoverflow.com/questions/37207668/how-do-i-open-a-materialize-sidenav-on-the-right-instead-of-the-left) to help me to get the sidenav menu to open on the right hand side of the screen.

* I used [Stack Overflow](https://stackoverflow.com/questions/36679649/how-to-add-a-color-overlay-to-a-background-image) to help with some issues I had with a background overlay.

* [Truncate Text](https://stackoverflow.com/questions/43999129/truncate-text-with-css) - I modified and used this code to suit my own needs in the project with the product description.

* I used the following [link](https://css-tricks.com/having-fun-with-link-hover-effects/) to help with hover effects on my logo.

* I used the following [link](https://stackoverflow.com/questions/2717480/css-selector-for-first-element-with-class) to help to target the first thumb up rating.

* The following [link](https://css-tricks.com/snippets/css/turn-off-number-input-spinners/) helped me to remove the number spinners on the right hand side of the numbers input box.

* The following [link](https://dev.to/atndesign/a-trick-to-change-the-autocomplete-background-color-21ll ) helped me to change the autofill color of the input fields, but I still could not get it to work correctly.

* I used the following [link](https://www.sanwebe.com/2013/03/addremove-input-fields-dynamically-with-jquery) to help to create a dynamic form that adds inputs to the array in the recipes database.

* The following [link](https://www.bootstrapfriendly.com/blog/dynamically-add-or-remove-form-input-fields-using-jquery/) was used to help remove input fields from the form

* I used the following [link](https://stackoverflow.com/questions/24597057/make-html-form-data-unchangeable-but-still-able-to-post#24597080) to add the session users to the input field automatically and not allow changes.

* I used the following [link](https://stackoverflow.com/questions/20233721/how-do-you-index-on-a-jinja-template) to help me with numbering in the loop.

* [input patterns](https://www.w3schools.com/TAGS/att_input_pattern.asp) were obtained and modified from here

* [List slicing with jinja](https://stackoverflow.com/questions/31301627/how-to-slice-a-sorted-list-in-jinja) used this to only dhow the first three ingredients in a recipe

* Needed help with displaying the correct recipes in the users profile using if statements and found guidance [here](https://stackoverflow.com/questions/42013067/how-to-access-session-variables-in-jinja-2-flask)

* Got some guidance and advice on pushing to mongoDb [here](https://docs.mongodb.com/manual/reference/operator/update/push/)

### Acknowledgements

* Slack user Igor - for helping me to understand why my delete modal was not working and helping me to fix the problem.

* My mentor Adegbenga adeye for his help and guidance throughout.

* Daisy - slack user, who helped me with try and except keyerror to understand what was wrong.

* Kenan - slack user, who helped me massively with pagination and implementing pagination on my site, he also provided guidance on the rating system I used.

* Karen - another slack user, Who helped me massively with my saving recipes and removing save of the recipes as I was having issues.
# Recipedia

![Mock-Up of the site]()

This is my 3rd milestone project for the Code Institute Full-Stack developer programme. I have chosen to do my project based on a cooking recipe website.

I decided to take inspiration from both the code institute student's handbook and my own interests to make a website dedicated to hosting recipes. it will allow users to log in and add their own recipes to the website and save other users recipes to their own profile for easy access and viewing.

I have made use of CRUD functionality throughout this project in allowing users to login, logout and register on the website. I also allow users to add recipes to the database, view other recipes, edit their own recipes that they have added to the website and delete their own recipes. the "admin" user has all functionality to the site icluding, adding, updating and deleting new products to the site and new categories.

A live preview of my site can be found [here](http://ms3-recipedia.herokuapp.com/get_recipes)

# Table of Contents

# UX

## Strategy

I created this project 

### goals

### user stories

## scope

### features

### future features

## structure

## skeleton

### wireframes

## surface

### colours

### images

### fonts

## Technologies Used

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

## Testing

### Html

### css

### javascript

### python

### user story Testing

### features Testing

## Deployment

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


## Credits

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
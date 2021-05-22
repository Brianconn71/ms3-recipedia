# Recipedia

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

### Media

### Code Snippets

### Acknowledgements
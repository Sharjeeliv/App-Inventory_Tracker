# Challenge-Shopify

Follow the below instructions to run the website locally. Alternatively the website is hosted on Heroku and can be viewed at
https://sharjeel-inventory-tracker.herokuapp.com

## Setup Instruction

### Requirments

Before running the website locally the following are required:

1. Python - Make sure you have python3 installed on your computer
2. Pip - This usually comes with python (check with pip --version) if not installed you will need to manually it from its website
3. virtualenv - This is a tool to manage python virtual environments it can be installed with **pip install virtualenv**

### Setup

If you have both python versions installed follows the commands as shows, otherwise if you only have python3 installed you will need to use 
python instead of python3. Similarly if you have both versions use pip3 in the command to install virtualenv otherwise used pip

1. Clone the repository to your local machine (either by using git or manually downloading it)
2. Open the terminal and move to the project folder
3. Create a virtual environemnt inside the project folder with this command: **python3 -m venv venv**
4. Activate the virtual environment: **source ./venv/bin/activate**
5. Install all the dependencies from the provided requirments.txt: **pip3 install -r ./requirements.txt**
6. The program can be launched locally with the following command: **python3 app.py**

## About The Website

This website uses the Flask framework for the backend implementation. The frontend is using the boostrap framework along with some custom CSS and HTML (utilized jinja2 which is the template engine for python. The data is all handled by SQLAlchemy (an ORM, the data is interacted with as a class) for flask which adds simple integration of a database to the website. The database used is SQLITE since it is bundled with python. For form functionality and validation WTForms was used. Pillows is a python library used for image operations.

## Notes on Extensibility

Flask Blueprint: A flask blueprint as like a 'mini' self contained web application. It handles its own routes and all functionallitY and these **"components"** are connected to the main application which grants the application all the functionality of the blueprint. *Blueprints can be completely self contained with all required files, however because of the smaller scale of this project HTML and CSS files are kept global.*

In essence a blueprint can be thought of as store bought RAM for a computer (the web app) that can be installed into the computer simply by plugging it in.

The program is designed utilizing blueprints and packages. The entire inventory functionality (forms, validation, database storage, etc.) are within the inventory blueprint. This improves code organization, readability, exstensibility, and reusability.

- **Organization & Readability** - The blueprint contains everything related to the inventory, from its forms, database template, functions, and routes. This naturally improves organization since everything is logically grouped. Readability has been improved by using SQLAlachmey and WTForms which represent the database and forms as classes (in python syntax). Additionally, conventions from PEP8 and Robert C. Martin (Clean Code) were used for elegent and readable code.

- **Extensibility** - This code can be extended by adding in other blueprints to extend functionality along with any required templates and CSS. Flask will automatically incorporate the blueprint into the greater web application for a seamless experience.

- **Reusability** - Similar to the above point, because of the blueprint this inventory functionality can be integrated into another flask web application.

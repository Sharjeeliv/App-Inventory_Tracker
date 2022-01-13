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

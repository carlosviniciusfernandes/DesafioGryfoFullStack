# Setting virtual env
py -3 -m venv venv

# Activation script
venv\Scripts\activate

# Variables
$env:FLASK_APP = "app"
$env:FLASK_ENV = "development"

# Install virtualenv if you haven't already
pip install virtualenv

# Create a virtual environment
virtualenv venv

# Activate the virtual environment (Windows)
venv\Scripts\activate

# Activate the virtual environment (Unix or MacOS)
source venv/bin/activate

# Please note that it can be pip3, python3 aswell depending on what version of python you are running

# Install Required Packages
pip install -r requirements.txt


# Run Your Flask App
python app.py

# Run the app
Open the index.html file in browser to get started
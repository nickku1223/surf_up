#import the flask dependency
from flask import Flask

# create a new Flask app instance
app = Flask(__name__)

# Define the starting point, as known as the root
@app.route('/') #The / denotes that we want to put our data at the root of our routes.
def hello_world():
    return 'Hello World' 

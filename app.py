#importing flask module in the project
from flask import Flask

#create an object of the flask class
app = Flask(__name__)

#the route function of the flask class
#"/"url is bound with first_flask function
@app.route("/")
def first_flask():
    return "This is my first flask program"

#run the application on local server
app.run()

#define a function with diffrent endpoints flask2

@app.route("/flask_2")
def second_flask():
    return "Python is fun"

app.run(debug = True)


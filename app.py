from flask import Flask
app = Flask(__name__)

@app.route('/')
def assepython():
    return 'Welcome to SCA Cloud School Application , this is my first assessment'

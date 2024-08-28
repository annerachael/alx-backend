from flask import Flask
""" import flask module """

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    """ define our root directory as index"""
    return "<title> Welcome to Holberton </title> <h1> Hello world </h1>"

if __name__ == "__main__":
    app.run(debug=True)

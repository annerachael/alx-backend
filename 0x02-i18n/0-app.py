from flask import Flask
""" import flask module """

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    """ define our root directory as index"""
    return render_template('0-index.html')

if __name__ == "__main__":
    app.run(debug=True)

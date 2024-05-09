import pathlib
from flask import Flask, render_template

basedir = pathlib.Path(__file__).parent.resolve()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
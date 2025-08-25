from flask import Flask, render_template
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
Scss(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/view')
def view_page():
    return render_template('view.html')

@app.route('/post')
def post_page():
    return render_template('post.html')

if __name__=="__main__":
    app.run(debug=True)
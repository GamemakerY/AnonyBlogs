from flask import Flask, render_template

app = Flask(__name__)


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
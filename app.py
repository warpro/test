from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('default.html')

@app.route('/test')
def test():
    return render_template('post.html')

@app.route('/post', methods=['post'])
def post():
    value = request.form['test']
    return render_template('default.html')

if __name__ == "__main__":
    app.run()

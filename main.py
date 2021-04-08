from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    '''Index page route'''

    return '<h1>Application Deployed!</h1>'

if __name__ == '__main__':
    app.run(debug=False)
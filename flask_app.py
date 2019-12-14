from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello'


@app.route('/health')
def health():
    return 'HTTP Status 200'


if __name__ == "__main__":
    app.run(debug=True)

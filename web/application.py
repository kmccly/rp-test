from flask import Flask, request


app = Flask(__name__)


@app.route("/")
def index():
    return app.send_static_file('index.html')


@app.route("/hello/")
def hello():
    return "Hello, world!";

if __name__ == "__main__":
    app.run()
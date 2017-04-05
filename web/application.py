from flask import Flask, request

from web import search


app = Flask(__name__)


@app.route("/")
def web_index():
    return app.send_static_file('index.html')


@app.route("/hello/")
def web_hello():
    return "Hello, world!"


@app.route("/search/")
def api_search():
    query = request.args.get('q')
    if query:
        return search.search(query)
    else:
        return ""


if __name__ == "__main__":
    app.run()
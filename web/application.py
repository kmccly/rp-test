from flask import Flask, request


app = Flask(__name__)


@app.route("/")
def index():
    return app.send_static_file('index.html')


@app.route("/search/")
def search():
    return """
    [
    {
        "city": "Westerlo", 
        "name": "David Harrington", 
        "country": "Spain", 
        "company": "Mattis Corporation", 
        "job_history": [
            "Sibelius"
        ], 
        "email": "vehicula@et.com"
    }, 
    {
        "city": "Osgoode", 
        "name": "Madeson Hopkins", 
        "country": "Tokelau", 
        "company": "Vitae Erat LLC", 
        "job_history": [
            "Chami"
        ], 
        "email": "non.arcu@dui.com"
    }, 
    {
        "city": "Gelbressee", 
        "name": "Nero Acosta", 
        "country": "Panama", 
        "company": "Lacus Cras Associates", 
        "job_history": [
            ""
        ], 
        "email": "tempus.non.lacinia@ultricesposuerecubilia.com"
    }, 
    {
        "city": "Westmount", 
        "name": "Ferris Yates", 
        "country": "Peru", 
        "company": "Eu Euismod Ac Corp.", 
        "job_history": [
            ""
        ], 
        "email": "scelerisque.scelerisque.dui@Nullamvitaediam.org"
    }, 
    {
        "city": "Cache Creek", 
        "name": "Germaine Griffin", 
        "country": "Oman", 
        "company": "Diam Sed Industries", 
        "job_history": [
            "Finale", 
            "Cakewalk"
        ], 
        "email": "dolor.Fusce@consectetueradipiscingelit.net"
    },] 
    """;

@app.route("/hello/")
def hello():
    return "Hello, world!";

if __name__ == "__main__":
    app.run()
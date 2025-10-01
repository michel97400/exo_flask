from flask import Flask
from flask import render_template
from flask import request
from markupsafe import escape
from flask import jsonify
import sqlite3
from flask import make_response
from flask import request

# Exo 1
app = Flask(__name__)

@app.route("/hello")
def home():
    return "Hello world"


# Exo 2 
@app.route("/contact")
def contact():
    return "<h1>Title</h1> <p>Paragraphe</p>"


# Exo 3
@app.route("/user/<name>")
def salue(name):
    return f'Salut {name}'


# Exo 4
@app.route("/jinja")
def base():
    return render_template("index.html")


# Exo 5
@app.route("/age", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        age = request.form["age"]
        return f"Tu as {escape(age)} ans!"
    return '''
        <form method="post">
            <input type="text" name="age">
            <input type="submit" value="Envoyer">
        </form>
    '''


# Exo 6
articles =[{"title": "Python is good", "author":"Moi"},
               {"title": "HTML is very good", "author":"Moi"}]

@app.route("/articles")
def article_list():
    return render_template('index.html', articles=articles)


# Exo 7
# index.html


# Exo 8
@app.route("/api/ping")
def main_api():
    var = { "ping": "pong" }
    return jsonify(var)


# Exo 9
@app.route("/user")
def add():
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
    cur.execute("INSERT INTO users VALUES (2,'joel')")
    con.commit()
    con.close()
    return f"Utilisateur ajouté !"


# Exo 10 
@app.route("/list_users")
def list():
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    con.commit()
    con.close()
    return users

# Exo 11
@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('404.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp

# Exo 12
@app.route("/search")
def requete():
    var = request.args.get('q')
    return f'Votre recherche: {var}'


# Exo 13 

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

simple_page = Blueprint('simple_page', __name__,
                        template_folder='templates')

@simple_page.route('/', defaults={'page': 'index'})
@simple_page.route('/<page>')
def show(page):
    try:
        return render_template(f'pages/{page}.html')
    except TemplateNotFound:
        abort(404)
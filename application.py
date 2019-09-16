from flask import Flask, render_template, url_for, redirect
from flask import request, jsonify, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Book

from flask import session as login_session
import random
import string

import httplib2
import json
import requests
from oauth2client.client import flow_from_clientsecrets, FlowExchangeError
from flask import make_response

# Init flask app
app = Flask(__name__)

# Creating SQLAlchemy connection with DB
engine = create_engine('sqlite:///bookstorecatalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# ID's
CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']

# Create a state token to prevent requery forgery.
# Store it in the session for later validation
@app.route("/login")
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in range(32))
    login_session['state'] = state
    return render_template("login.html", STATE=state)

# Google Logout
@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])

    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('User is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;'
    output += 'border-radius: 150px;'
    output += '-webkit-border-radius: 150px;-moz-border-radius: 150px;">'
    flash("You are now logged in as %s" % login_session['username'])
    print "done!"
    return output


# Disconnect Google User
@app.route('/gdisconnect')
def gdisconnect():
    access_token = login_session.get('access_token')
    if access_token is None:
        print 'Access Token is None'
        response = make_response(json.dumps('User not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s'\
          % login_session['access_token']
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps('Failed to revoke token.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response

# URL routing
@app.route("/")
@app.route("/catalog", methods=["GET"])
def catalog():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    categories = session.query(Category).all()
    books = session.query(Book).all()
    latestbooks = books[-11:]
    latestbooks.reverse()
    return render_template("catalog.html",
                           categories=categories,
                           books=latestbooks)


@app.route("/catalog/<int:category_id>/items")
def category(category_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    category = session.query(Category).filter_by(id=category_id).one()
    books = session.query(Book).filter_by(category_id=category_id).all()
    categories = session.query(Category).all()
    return render_template("category.html",
                           category=category,
                           books=books,
                           categories=categories)


@app.route("/catalog/<int:category_id>/<int:book_id>")
def book(category_id, book_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    category = session.query(Category).filter_by(id=category_id).one()
    book = session.query(Book).filter_by(id=book_id).one()
    return render_template("book.html", book=book, category=category)

# CRUD Routing
@app.route("/catalog/new", methods=["GET", "POST"])
def newBook():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    categories = session.query(Category).all()
    if request.method == "POST":
        category = session.query(Category).filter_by(
            name=request.form["category"]).one()
        newBook = Book(title=request.form["title"],
                       category=category,
                       description=request.form["description"])
        session.add(newBook)
        session.commit()
        flash("New Book Created.")
        return redirect(url_for('catalog'))
    return render_template("new.html", categories=categories)


@app.route("/catalog/<int:category_id>/<int:book_id>/edit",
           methods=["GET", "POST"])
def editBook(book_id, category_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    editedbook = session.query(Book).filter_by(id=book_id).one()
    if request.method == "POST":
        editedbook.title = request.form['newtitle']
        session.add(editedbook)
        session.commit()
        flash("Book has been edited.")
        return redirect(url_for('catalog'))
    return render_template("edit.html",
                           book=editedbook,
                           category=category_id)


@app.route("/catalog/<int:category_id>/<int:book_id>/delete",
           methods=["GET", "POST"])
def deleteBook(book_id, category_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    deletedbook = session.query(Book).filter_by(id=book_id).one()
    if request.method == "POST":
        session.delete(deletedbook)
        session.commit()
        flash("Book has been deleted")
        return redirect(url_for('catalog'))
    return render_template("delete.html", book=deletedbook)


# API endpoits
@app.route("/catalog/categories/JSON")
def categoriesJSON():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    categories = session.query(Category).all()
    return jsonify(Categories=[category.serialize for category in categories])


@app.route("/catalog/books/JSON")
def booksJSON():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    books = session.query(Book).all()
    return jsonify(Books=[book.serialize for book in books])


# End of File
if __name__ == "__main__":
    app.secret_key = "super_secret_key"
    app.debug = True
    app.run("0.0.0.0", port=8000, threaded=False)

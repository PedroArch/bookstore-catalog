from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Book

# Init flask app
app = Flask(__name__)

# Creating SQLAlchemy connection with DB
engine = create_engine('sqlite:///bookstorecatalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# URL routing
@app.route("/")
@app.route("/catalog")
def catalog():
    return "Catalog main page."


@app.route("/catalog/<int:category_id>/items")
def category(category_id):
    return "%s books category" % category.name


@app.route("/catalog/<int:category_id>/<int:book_id>")
def book(category_id, book_id):
    return "%s description page" % book.name

# CRUD Routing
@app.route("/catalog/new")
def newBook():
    return "New book page"


@app.route("/catalog/<int:category_id>/<int:book_id>/edit")
def editBook(book_id):
    return "%s edit page" % editedbook.name


@app.route("/catalog/<int:category_id>/<int:book_id>/delete")
def deleteBook(book_id):
    return "% delete page" % deletedbook.name

# Not Found Page
@app.route("/catalog/notfound")
def notFound():
    return "Not Found Page"

# End of File
if __name__ == "__main__":
    app.debug = True
    app.run("0.0.0.0", port=8000)
from flask import Flask, render_template, url_for
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
@app.route("/catalog", methods=["GET"])
def catalog():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    categories = session.query(Category).all()
    books = session.query(Book).all()
    latestbooks = books[-11:]
    return render_template("catalog.html", categories=categories, books=latestbooks)


@app.route("/catalog/<int:category_id>/items")
def category(category_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    category = session.query(Category).filter_by(id=category_id).one()
    books = session.query(Book).filter_by(category_id=category_id).all()
    categories = session.query(Category).all()
    return render_template("category.html", category = category, books = books, categories = categories)


@app.route("/catalog/<int:category_id>/<int:book_id>")
def book(category_id, book_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    category = session.query(Category).filter_by(id=category_id).one()
    book = session.query(Book).filter_by(id=book_id).one()
    return render_template("book.html", book = book, category=category)

# CRUD Routing
@app.route("/catalog/new", methods=["GET", "POST"])
def newBook():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    categories = session.query(Category).all()
    return render_template("new.html", categories = categories)


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

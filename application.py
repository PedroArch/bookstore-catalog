from flask import Flask, render_template, url_for, redirect, request
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
    latestbooks.reverse()
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
    if request.method == "POST":
        category = session.query(Category).filter_by(name=request.form["category"]).one()
        newBook = Book(
        title=request.form["title"],
        category=category,
        description=request.form["description"])
        session.add(newBook)
        session.commit()
        return redirect(url_for('catalog'))
    return render_template("new.html", categories=categories)


@app.route("/catalog/<int:category_id>/<int:book_id>/edit", methods=["GET", "POST"])
def editBook(book_id, category_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    editedbook = session.query(Book).filter_by(id=book_id).one()
    if request.method == "POST":
        editedbook.title = request.form['newtitle']
        session.add(editedbook)
        session.commit()
        return redirect(url_for('catalog'))
    return render_template("edit.html", book = editedbook, category=category_id)


@app.route("/catalog/<int:category_id>/<int:book_id>/delete", methods=["GET", "POST"])
def deleteBook(book_id, category_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    deletedbook = session.query(Book).filter_by(id=book_id).one()
    if request.method == "POST":
        session.delete(deletedbook)
        session.commit()
        return redirect(url_for('catalog'))
    return render_template("delete.html", book = deletedbook)


# End of File
if __name__ == "__main__":
    app.debug = True
    app.run("0.0.0.0", port=8000)

from flask import Flask, render_template, Blueprint, request, redirect
from repositories import book_repository, author_repository
from models.book import Book

books_blueprint = Blueprint("books", __name__)

# INDEX
# GET BOOKS
@books_blueprint.route('/books')
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books = books)

# NEW
# GET '/books/new'
@books_blueprint.route('/books/new')
def new_book():
    authors = author_repository.select_all()
    return render_template("books/new.html", all_authors = authors)

# CREATE
# POST '/books'
@books_blueprint.route('/books', methods=['POST'])
def create_book():
    title = request.form['title']
    author = author_repository.select(request.form['author'])
    genre = request.form['genre']
    publisher = request.form['publisher']
    page_count = request.form['page_count']
    book = Book(title, author, genre, publisher, page_count)
    book_repository.save(book)
    return redirect ("/books")

# SHOW
# GET '/books/<id>'
@books_blueprint.route('/books/<id>')
def show_book(id):
    book = book_repository.select(id)
    return render_template("books/show.html", book = book)


# EDIT
# GET '/books/<id>/edit'
@books_blueprint.route('/books/edit/<id>')
def edit_book(id):
    authors = author_repository.select_all()
    book = book_repository.select(id)
    return render_template("books/edit.html", all_authors = authors, book = book)

# UPDATE
# PUT '/books/<id>'
@books_blueprint.route("/books/<id>", methods=['POST'])
def update_book(id):
    title = request.form['title']
    author = author_repository.select(request.form['author'])
    genre = request.form['genre']
    publisher = request.form['publisher']
    page_count = request.form['page_count']
    book = Book(title, author, genre, publisher, page_count, id)
    book_repository.update(book)
    return redirect ("/books")

# DELETE
# DELETE '/books/<id>'
@books_blueprint.route("/books/<id>/delete", methods=['POST'])
def delete_book(id):
    book_repository.delete(id)
    return redirect ("/books")
from db.run_sql import run_sql
from models.book import Book
from models.author import Author
import repositories.author_repository as author_repository

def save(book):
    sql = "INSERT INTO books (title, author_id, genre, publisher, page_count) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    author_id = book.author.id
    values = [book.title, author_id, book.genre, book.publisher, book.page_count]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

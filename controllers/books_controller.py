from flask import Flask, render_template, Blueprint, request, redirect
from repositories import book_repository, author_repository
from models.book import Book

books_blueprint = Blueprint("books", __name__)
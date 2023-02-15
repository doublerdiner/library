class Book:
    def __init__(self, title, author, genre, publisher, page_count, id = None):
        self.title = title
        self.author = author
        self.genre = genre
        self.publisher = publisher
        self.page_count = page_count
        self.id = id
import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

# book_repository.delete_all()
author_repository.delete_all()

author_1 = Author("Stephen King")
author_2 = Author("Michel Faber")
author_repository.save(author_1)
author_repository.save(author_2)
author_repository.select_all()

author_repository.delete(author_1.id)

author_2.name = "David Mitchell"
author_repository.update(author_2)

print(author_repository.books(author_1))


# book_1 = Book("The Shining", author_1, "Horror", "Hoddor", 512)
# book_2 = Book("11.22.63", author_1, "Science Fiction", "Hoddor", 752)
# book_3 = Book("The Dark Tower: The Gunslinger", author_1, "Fantasy", 304)
# book_4 = Book("Under the Skin", author_2, "Science Fiction", "Canongate Books", 306)
# book_5 = Book("The Book of Strange New Things", author_2, "Science Fiction", "Canongate Books", 592)
# book_repository.save(book_1)
# book_repository.save(book_2)
# book_repository.save(book_3)
# book_repository.save(book_4)
# book_repository.save(book_5)

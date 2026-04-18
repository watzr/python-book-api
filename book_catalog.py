from dataclasses import dataclass

@dataclass
class Book:
    isbn: str
    title: str
    author: str
    genre: str
    year_published: int
        
BOOKS = [
    Book("978-3-16-148410-0", "The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 1925),
    Book("978-0-14-028333-4", "To Kill a Mockingbird", "Harper Lee", "Fiction", 1960),
    Book("978-0-452-28423-4", "1984", "George Orwell", "Dystopian", 1949),
    Book("978-0-7432-7356-5", "The Catcher in the Rye", "J.D. Salinger", "Fiction", 1951),
    Book("978-0-14-044913-6", "The Odyssey", "Homer", "Epic", -800),
    Book("978-0-14-044927-3", "The Iliad", "Homer", "Epic", -750),
    Book("978-0-14-044926-6", "The Aeneid", "Virgil", "Epic", -19),
    Book("978-0-14-044918-1", "The Divine Comedy", "Dante Alighieri", "Epic", 1320),
    Book("978-0-14-044919-8", "The Canterbury Tales", "Geoffrey Chaucer", "Poetry", 1400),
    Book("978-0-14-044920-4", "The Metamorphosis", "Franz Kafka", "Fiction", 1915),
    Book("978-0-14-044921-1", "The Trial", "Franz Kafka", "Fiction", 1925),
    Book("978-0-14-044922-8", "The Castle", "Franz Kafka", "Fiction", 1926),
    Book("978-0-14-044923-5", "The Stranger", "Albert Camus", "Fiction", 1942),
    Book("978-0-14-044924-2", "The Plague", "Albert Camus", "Fiction", 1947),
    Book("978-0-14-044925-9", "The Fall", "Albert Camus", "Fiction", 1956),
    Book("978-0-14-044926-6", "The Myth of Sisyphus", "Albert Camus", "Philosophy", 1942),
    Book("978-0-14-044927-3", "The Rebel", "Albert Camus", "Philosophy", 1951),
    Book("978-0-14-044928-0", "The Plague", "Albert Camus", "Fiction", 1947),
    Book("978-0-14-044929-7", "The Fall", "Albert Camus", "Fiction", 1956),
    Book("978-0-14-044930-3", "The Myth of Sisyphus", "Albert Camus", "Philosophy", 1942),
    Book("978-0-14-044931-0", "The Rebel", "Albert Camus", "Philosophy", 1951)
    ]

# This function returns a list of Book objects
def get_book_catalog():
    return BOOKS

def find_book_by_isbn(isbn):
    for book in BOOKS:
        if book.isbn == isbn:
            return book
    return None

def find_books_by_author(author):
    return [book for book in BOOKS if book.author == author]

def find_books_by_genre(genre):
    return [book for book in BOOKS if book.genre == genre]

def find_books_by_year(year):
    return [book for book in BOOKS if book.year_published == year]

def find_books_by_title(title):
    return [book for book in BOOKS if book.title == title]

def find_books_by_keyword(keyword):
    return [book for book in BOOKS if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()]

def add_book(isbn, title, author, genre, year_published):
    new_book = Book(isbn, title, author, genre, year_published)
    BOOKS.append(new_book)

def remove_book(isbn):
    global BOOKS
    BOOKS = [book for book in BOOKS if book.isbn != isbn]

def update_book(isbn, title=None, author=None, genre=None, year_published=None):
    book = find_book_by_isbn(isbn)
    if book:
        if title:
            book.title = title
        if author:
            book.author = author
        if genre:
            book.genre = genre
        if year_published:
            book.year_published = year_published

def count_books():
    return len(BOOKS)

def print_book_catalog():
    for book in BOOKS:
        print(f"ISBN: {book.isbn}, Title: {book.title}, Author: {book.author}, Genre: {book.genre}, Year Published: {book.year_published}")


def main():
    print("Get all books:")
    print_book_catalog()
    print(f"Total books in catalog: {len(get_book_catalog())}")
    print(find_book_by_isbn("978-3-16-148410-0"))
    print(find_books_by_author("F. Scott Fitzgerald"))
    print(find_books_by_genre("Fiction"))
    print(find_books_by_year(1925))
    print(find_books_by_title("The Great Gatsby"))
    print(find_books_by_keyword("Gatsby"))
    add_book("978-0-14-044927-3", "The Rebel", "Albert Camus", "Philosophy", 1951)
    print(find_book_by_isbn("978-0-14-044927-3"))
    print("Get all books:")
    print_book_catalog()
    remove_book("978-0-14-044927-3")
    print("Uopdate book:")
    update_book("978-0-14-044927-3", "The Rebel", "Albert Camus", "Philosophy", 1951)
    print(find_book_by_isbn("978-0-14-044927-3"))
    print("Get all books:")
    print_book_catalog()
    print(f"Total books in catalog: {count_books()}")

if __name__ == "__main__":
    main()
from fastapi import FastAPI, HTTPException
from book_catalog import get_book_catalog, find_book_by_isbn, find_books_by_author, find_books_by_genre, find_books_by_year

app = FastAPI(title="Book Catalog API", description="API for managing book catalog", version="1.0.0")

@app.get("/")
def index():
    """Welcome to the Book Catalog API! Use the endpoints to explore the book catalog."""
    return {"message": "Welcome to the Book Catalog API! Use the endpoints to explore the book catalog."}

@app.get("/books", response_model=list[dict])
def get_all_books():
    """Get all books in the catalog"""
    books = get_book_catalog()
    return [book.__dict__ for book in books]

@app.get("/books/{isbn}", response_model=dict)
def get_book_by_isbn(isbn: str):
    """Get a book by its ISBN"""
    book = find_book_by_isbn(isbn)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book.__dict__

@app.get("/books/author/{author}", response_model=list[dict])
def get_books_by_author(author: str):
    """Get books by author"""
    books = find_books_by_author(author)
    return [book.__dict__ for book in books]

@app.get("/books/genre/{genre}", response_model=list[dict])
def get_books_by_genre(genre: str):
    """Get books by genre"""
    books = find_books_by_genre(genre)
    return [book.__dict__ for book in books]

@app.get("/books/year/{year}", response_model=list[dict])
def get_books_by_year(year: int):
    """Get books by publication year"""
    books = find_books_by_year(year)
    return [book.__dict__ for book in books]
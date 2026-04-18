# Book Catalog API

A FastAPI application that exposes book catalog functions via REST endpoints.

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the API

Start the server with:
```bash
uvicorn api:app --reload
```

The API will be available at `http://127.0.0.1:8000`

## API Endpoints

- `GET /books` - Get all books
- `GET /books/{isbn}` - Get book by ISBN
- `GET /books/author/{author}` - Get books by author
- `GET /books/genre/{genre}` - Get books by genre
- `GET /books/year/{year}` - Get books by publication year

## Documentation

Interactive API documentation is available at `http://127.0.0.1:8000/docs`
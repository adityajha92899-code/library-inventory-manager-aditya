
import json
from pathlib import Path
from book import Book


class LibraryInventory:
    def __init__(self, file_path="books.json"):
        self.file_path = Path(file_path)
        self.books = []
        self.load_books()

    def load_books(self):
        if self.file_path.exists():
            try:
                with open(self.file_path, "r") as file:
                    data = json.load(file)
                    for item in data:
                        self.books.append(Book(**item))
            except:
                print("Error reading file. Starting with empty list.")

    def save_books(self):
        with open(self.file_path, "w") as file:
            json.dump([book.to_dict() for book in self.books], file, indent=4)

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def search_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]

    def search_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def display_all(self):
        for book in self.books:
            print(book)

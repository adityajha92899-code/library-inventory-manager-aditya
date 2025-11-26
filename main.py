from inventory import LibraryInventory
from book import Book

library = LibraryInventory()

def menu():
    while True:
        print("\n--- Library Inventory Manager ---")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search Book")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            book = Book(title, author, isbn)
            library.add_book(book)
            print("Book added successfully!")

        elif choice == "2":
            isbn = input("Enter ISBN to issue: ")
            book = library.search_by_isbn(isbn)
            if book and book.issue():
                library.save_books()
                print("Book issued successfully!")
            else:
                print("Book not available.")

        elif choice == "3":
            isbn = input("Enter ISBN to return: ")
            book = library.search_by_isbn(isbn)
            if book and book.return_book():
                library.save_books()
                print("Book returned!")
            else:
                print("Invalid operation.")

        elif choice == "4":
            library.display_all()

        elif choice == "5":
            term = input("Enter title to search: ")
            results = library.search_by_title(term)
            for b in results:
                print(b)

        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")

menu()

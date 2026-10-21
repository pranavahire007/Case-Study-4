
# Library Book Search System Using Hashing
# Data Structures Case Study - Unit IV

TABLE_SIZE = 10


class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    # Hash function to calculate the index
    def hash_function(self, book_id):
        return sum(ord(char) for char in str(book_id)) % self.size

    # Add a new book
    def add_book(self, book_id, title, author):
        index = self.hash_function(book_id)
        bucket = self.table[index]

        # Update the book if its ID already exists
        for book in bucket:
            if book.book_id == book_id:
                book.title = title
                book.author = author
                print("Book updated successfully!")
                return

        # Separate chaining handles collisions
        bucket.append(Book(book_id, title, author))
        print("Book added successfully!")

    # Search for a book by ID
    def search_book(self, book_id):
        index = self.hash_function(book_id)

        for book in self.table[index]:
            if book.book_id == book_id:
                print("\nBook Found!")
                print("Book ID :", book.book_id)
                print("Title   :", book.title)
                print("Author  :", book.author)
                return

        print("Book not found.")

    # Delete a book by ID
    def delete_book(self, book_id):
        index = self.hash_function(book_id)
        bucket = self.table[index]

        for book in bucket:
            if book.book_id == book_id:
                bucket.remove(book)
                print("Book deleted successfully!")
                return

        print("Book not found.")

    # Display all books
    def display_books(self):
        print("\n========== Library Books ==========")
        found = False

        for index, bucket in enumerate(self.table):
            if bucket:
                for book in bucket:
                    found = True
                    print(
                        f"Index: {index} | "
                        f"Book ID: {book.book_id} | "
                        f"Title: {book.title} | "
                        f"Author: {book.author}"
                    )

        if not found:
            print("No books available.")

        print("===================================")

    # Display hash table buckets
    def display_hash_table(self):
        print("\n========== Hash Table ==========")

        for index, bucket in enumerate(self.table):
            book_ids = [book.book_id for book in bucket]
            print(f"Index {index}: {book_ids}")

        print("================================")


def main():
    library = HashTable(TABLE_SIZE)

    while True:
        print("\n===== Library Book Search System =====")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Delete Book")
        print("4. Display All Books")
        print("5. Display Hash Table")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            book_id = input("Enter Book ID: ").strip()
            if not book_id:
                print("Book ID cannot be empty.")
                continue

            title = input("Enter Book Title: ").strip()
            author = input("Enter Author Name: ").strip()

            if not title or not author:
                print("Title and author cannot be empty.")
                continue

            library.add_book(book_id, title, author)

        elif choice == "2":
            book_id = input("Enter Book ID to search: ").strip()
            library.search_book(book_id)

        elif choice == "3":
            book_id = input("Enter Book ID to delete: ").strip()
            library.delete_book(book_id)

        elif choice == "4":
            library.display_books()

        elif choice == "5":
            library.display_hash_table()

        elif choice == "6":
            print("Thank you for using the Library Book Search System!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()

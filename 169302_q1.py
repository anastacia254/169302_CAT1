class Book:
    def __init__(this, title, author):
        this.title = title
        this.author = author
        this.is_borrowed = False

    def mark_as_borrowed(this):
        if not this.is_borrowed:
            this.is_borrowed = True
            return True
        return False

    def mark_as_returned(this):
        if this.is_borrowed:
            this.is_borrowed = False
            return True
        return False

    def __str__(this):
        return f"'{this.title}' by {this.author} {'(Borrowed)' if this.is_borrowed else '(Available)'}"


class LibraryMember:
    def __init__(this, name, member_id):
        this.name = name
        this.member_id = member_id
        this.borrowed_books = []

    def borrow_book(this, book):
        if book.mark_as_borrowed():
            this.borrowed_books.append(book)
            print(f"{this.name} borrowed '{book.title}'.")
        else:
            print(f"'{book.title}' is currently borrowed by someone else.")

    def return_book(this, book):
        if book in this.borrowed_books:
            book.mark_as_returned()
            this.borrowed_books.remove(book)
            print(f"{this.name} returned '{book.title}'.")
        else:
            print(f"{this.name} has not borrowed '{book.title}'.")

    def list_borrowed_books(this):
        if not this.borrowed_books:
            print(f"{this.name} has not borrowed any books.")
        else:
            print(f"{this.name}'s borrowed books:")
            for book in this.borrowed_books:
                print(f" - {book.title} by {book.author}")

    def __str__(this):
        return f"Library Member: {this.name}, ID: {this.member_id}"


# Example Books
book1 = Book("Grave of fireflies", "Akiyuki Nosaka")
book2 = Book("The boy and the heroin", "Hayao Miyazaki")
book3 = Book("Stranger things", "Duffer Brothers")

# Example Member
member = LibraryMember("Sanora", "M001")

# Interactive Code
while True:
    print("\nLibrary System")
    print("1. Borrow a Book")
    print("2. Return a Book")
    print("3. List Borrowed Books")
    print("4. View All Books")
    print("5. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        print("\nAvailable Books:")
        for book in [book1, book2, book3]:
            if not book.is_borrowed:
                print(f" - {book}")

        title = input("Enter the title of the book to borrow: ")
        for book in [book1, book2, book3]:
            if book.title == title:
                member.borrow_book(book)
                break
        else:
            print(f"'{title}' is not available in the library.")

    elif choice == "2":
        print("\nBorrowed Books:")
        member.list_borrowed_books()
        title = input("Enter the title of the book to return: ")
        for book in member.borrowed_books:
            if book.title == title:
                member.return_book(book)
                break
        else:
            print(f"{title} is not in your borrowed books.")

    elif choice == "3":
        member.list_borrowed_books()

    elif choice == "4":
        print("\nAll Books:")
        for book in [book1, book2, book3]:
            print(f" - {book}")

    elif choice == "5":
        print("Exiting the library system.")
        break

    else:
        print("Invalid choice. Please try again.")

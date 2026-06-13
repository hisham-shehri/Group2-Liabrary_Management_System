from library_system import Book, Member, StudentMember, StaffMember, Library

def add_new_book(lib):
    isbn = input("Enter book ISBN: ")
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = input("Enter publication year: ")
    genre = input("Enter book genre: ")
    lib.add_book(Book(title, author, year, isbn, genre))

def register_new_member(lib):
    m_id = input("Enter member ID: ")
    name = input("Enter member name: ")
    m_type = input("Is this a Student (1) or Staff (2)? ")
    
    if m_type == '1':
        lib.register_member(StudentMember(name, int(m_id)))
    elif m_type == '2':
        lib.register_member(StaffMember(name, int(m_id)))
    else:
        print("Invalid type. Registering as a standard Member.")
        lib.register_member(Member(name, int(m_id)))

def borrow_book_feature(lib):
    isbn = input("Enter book ISBN to borrow: ")
    m_id = input("Enter member ID: ")
    lib.borrow_book(isbn, m_id)

def return_book_feature(lib):
    isbn = input("Enter book ISBN to return: ")
    m_id = input("Enter member ID: ")
    lib.return_book(isbn, m_id)

def search_by_title(lib):
    title = input("Enter book title to search: ")
    lib.search_by_title(title)

def show_all(lib):
    lib.show_all()

def show_statistics(lib):
    lib.show_statistics()

def delete_book_feature(lib):
    isbn = input("Enter the ISBN of the book to delete: ")
    lib.delete_book(isbn)


def main():
    library = Library()

    raw_books = [
        ("The Pragmatic Programmer", "Andrew Hunt", 1999, "978-0201616224", "Programming"),
        ("Crime and Punishment", "Fyodor Dostoevsky", 1866, "978-0140449136", "Classic"),
        ("Dune", "Frank Herbert", 1965, "978-0441172719", "Sci-Fi")
    ]
    
    for title, author, year, isbn, genre in raw_books:
        library.books.append(Book(title, author, year, isbn, genre))
        library.genres.add(genre)

    library.members[101] = StudentMember("Sara Al-Otaibi", 101)
    library.members[102] = StudentMember("Fahad Al-Dossari", 102)
    library.members[201] = StaffMember("Dr. Ahmad", 201)
    library.members[202] = StaffMember("Prof. Noura", 202)
    print("Ready-made data loaded successfully!\n")
    # ------------------------------------------

    while True:
        print("\n=== Library Management System ===")
        print("1. Add a New Book")
        print("2. Register a New Member")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Search by Title")
        print("6. Show All Books")
        print("7. Show Statistics")
        print("8. Delete a Book")
        print("9. Exit")
        
        choice = input("Enter your choice: ")
        
        match choice:
            case "1": add_new_book(library)
            case "2": register_new_member(library)
            case "3": borrow_book_feature(library)
            case "4": return_book_feature(library)
            case "5": search_by_title(library)
            case "6": show_all(library)
            case "7": show_statistics(library)
            case "8": delete_book_feature(library)
            case "9": 
                print("Goodbye!")
                break
            case _: 
                print("Invalid choice, please try again.")
        
        if choice != "9":
            input("\nPress Enter to return to the menu...")

if __name__ == "__main__":
    main()
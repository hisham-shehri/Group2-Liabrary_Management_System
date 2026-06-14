from datetime import datetime, timedelta


class Book:
    def __init__(self, title, author, year, isbn, genre):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn  
        self.genre = genre
        self.is_borrowed = False
        self.due_date = None


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
        self._late_fees = 0   

    def borrow_limit(self):
        return 0

    def get_fees(self):
        return self._late_fees

    def add_fee(self, amount):
        self._late_fees += amount

    def display(self):
        print(f"{self.member_id} | {self.name} | Books: {len(self.borrowed_books)} | Fees: {self._late_fees}")


class StudentMember(Member):
    def borrow_limit(self):
        return 3


class StaffMember(Member):
    def borrow_limit(self):
        return 10


class Library:
    def __init__(self):
        self.books = []
        self.members = {}  
        self.genres = set()

    
    def add_book(self, book):
        self.books.append(book)
        self.genres.add(book.genre)
        print(f"Book added successfully: {book.title}")

    def delete_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book '{book.title}' deleted successfully.")
                return
        print("Sorry, the book is not found in the system.")

    def delete_member(self, member_id):
        try:
            m_id = int(member_id)
        except ValueError:
            print("Invalid Member ID format.")
            return

        member = self.members.get(m_id)

        if not member:
            print("Member not found.")
            return

        del self.members[m_id]
        print(f"Member '{member.name}' deleted successfully.")


    def register_member(self, member):
        self.members[member.member_id] = member
        print(f"Member registered successfully: {member.name}")

    
    def borrow_book(self, isbn, member_id):

        try:
            m_id = int(member_id)
        except ValueError:
            print("Invalid Member ID format.")
            return

        member = self.members.get(m_id)
        book = next((b for b in self.books if b.isbn == isbn), None)

        if not member:
            print("Member is not registered in the system.")
            return
        if not book:
            print("Book is not found in the library.")
            return
        if book.is_borrowed:
            print("The book is currently borrowed.")
            return

        
        if len(member.borrowed_books) >= member.borrow_limit():
            print("Borrow limit reached!")
            return

        book.is_borrowed = True
        book.due_date = datetime.now() + timedelta(days=7)
        member.borrowed_books.append(book)

        due_date_str = book.due_date.strftime("%Y-%m-%d")
        print(f"Book '{book.title}' borrowed successfully.")
        print(f"**Alert:** Must be returned by: {due_date_str}")

    def return_book(self, isbn, member_id,days_late):

        try:
            m_id = int(member_id)
        except ValueError:
            print("Invalid Member ID format.")
            return

        member = self.members.get(m_id)
        book = next((b for b in self.books if b.isbn == isbn), None)

        if not member or not book:
            print("Invalid Member ID or Book ISBN.")
            return

        if book not in member.borrowed_books:
            print("This book was not borrowed by this member.")
            return

        member.borrowed_books.remove(book)
        book.is_borrowed = False

        days_late = 0
        fee = days_late * 2
        member.add_fee(fee)

        print(f"Book '{book.title}' returned successfully.")
        print(f"Late fee: {fee} SAR | Total fees: {member.get_fees()} SAR")

    def search_by_title(self, title):
        found_books = [b for b in self.books if title.lower() in b.title.lower()]
        if found_books:
            for b in found_books:
                status = "Borrowed" if b.is_borrowed else "Available"
                print(f"ISBN: {b.isbn} | Title: {b.title} | Author: {b.author} | Genre: {b.genre} | Status: {status}")
        else:
            print("No books found with that title.")

    def show_all_books(self):
        if not self.books:
            print("The library is currently empty.")
            return

        for b in self.books:
            status = "Borrowed" if b.is_borrowed else "Available"
            print(f"ISBN: {b.isbn} | Title: {b.title} | Status: {status}")


    def show_all_members(self):
        if not self.members:
            print("No members found.")
            return

        for m in self.members.values():
            m.display()

    def show_statistics(self):
        total_books = len(self.books)
        borrowed_books = sum(1 for b in self.books if b.is_borrowed)
        available_books = total_books - borrowed_books

        print("\n--- Library Statistics ---")
        print(f"Total Books: {total_books}")
        print(f"Available Books: {available_books}")
        print(f"Borrowed Books: {borrowed_books}")
        print(f"Total Members: {len(self.members)}")
        print(f"Total Genres: {len(self.genres)}")
        print("--------------------------")

# Library Management System

# Features:
# 1. Book and Member Management
# 2. Book Borrowing and Returns
# 3. Fine Calculation
# 4. Search Functionality
# 5. Book Recommendations

from datetime import datetime, timedelta
import json
import random

class Book:
    """Represents a book in the library"""
    def __init__(self, title, author, isbn, category, copies=1):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.category = category
        self.total_copies = copies
        self.available_copies = copies
        self.borrowers = []  # List of current borrowers
        self.ratings = []    # List of ratings (1-5 stars)
    
    def to_dict(self):
        """Convert book to dictionary for JSON storage"""
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "category": self.category,
            "total_copies": self.total_copies,
            "available_copies": self.available_copies,
            "borrowers": self.borrowers,
            "ratings": self.ratings
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create book from dictionary"""
        book = cls(data["title"], data["author"], data["isbn"], data["category"], data["total_copies"])
        book.available_copies = data["available_copies"]
        book.borrowers = data["borrowers"]
        book.ratings = data["ratings"]
        return book

class Member:
    """Represents a library member"""
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = {}  # ISBN: borrow_date
        self.history = []        # List of past borrows
        self.fines = 0.0        # Total unpaid fines
    
    def to_dict(self):
        """Convert member to dictionary for JSON storage"""
        return {
            "name": self.name,
            "member_id": self.member_id,
            "borrowed_books": {k: v.strftime("%Y-%m-%d") for k, v in self.borrowed_books.items()},
            "history": self.history,
            "fines": self.fines
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create member from dictionary"""
        member = cls(data["name"], data["member_id"])
        member.borrowed_books = {k: datetime.strptime(v, "%Y-%m-%d") 
                               for k, v in data["borrowed_books"].items()}
        member.history = data["history"]
        member.fines = data["fines"]
        return member

class Library:
    """Library management system"""
    def __init__(self, name):
        self.name = name
        self.books = {}      # ISBN: Book
        self.members = {}    # member_id: Member
        self.loan_period = 14  # Days
        self.fine_per_day = 1.0  # Dollar per day
        self.load_data()
    
    def load_data(self):
        """Load library data from JSON files"""
        try:
            # Load books
            with open("books.json", "r") as f:
                books_data = json.load(f)
                self.books = {isbn: Book.from_dict(data) 
                            for isbn, data in books_data.items()}
            
            # Load members
            with open("members.json", "r") as f:
                members_data = json.load(f)
                self.members = {id_: Member.from_dict(data) 
                              for id_, data in members_data.items()}
        except FileNotFoundError:
            pass
    
    def save_data(self):
        """Save library data to JSON files"""
        # Save books
        with open("books.json", "w") as f:
            books_data = {isbn: book.to_dict() 
                         for isbn, book in self.books.items()}
            json.dump(books_data, f, indent=4)
        
        # Save members
        with open("members.json", "w") as f:
            members_data = {id_: member.to_dict() 
                          for id_, member in self.members.items()}
            json.dump(members_data, f, indent=4)
    
    def add_book(self, title, author, isbn, category, copies=1):
        """Add a new book to the library"""
        if isbn in self.books:
            self.books[isbn].total_copies += copies
            self.books[isbn].available_copies += copies
            return {"status": "success", "message": f"Added {copies} copies of existing book"}
        
        book = Book(title, author, isbn, category, copies)
        self.books[isbn] = book
        self.save_data()
        return {"status": "success", "message": "Book added successfully"}
    
    def add_member(self, name):
        """Register a new member"""
        member_id = str(random.randint(10000, 99999))
        while member_id in self.members:
            member_id = str(random.randint(10000, 99999))
        
        member = Member(name, member_id)
        self.members[member_id] = member
        self.save_data()
        return {"status": "success", "message": f"Member registered successfully", "member_id": member_id}
    
    def borrow_book(self, member_id, isbn):
        """Process book borrowing"""
        if isbn not in self.books or member_id not in self.members:
            return {"status": "error", "message": "Invalid book or member ID"}
        
        book = self.books[isbn]
        member = self.members[member_id]
        
        if book.available_copies == 0:
            return {"status": "error", "message": "Book not available"}
        
        if len(member.borrowed_books) >= 3:
            return {"status": "error", "message": "Maximum borrow limit reached"}
        
        if member.fines > 0:
            return {"status": "error", "message": f"Please clear outstanding fine of ${member.fines:.2f}"}
        
        book.available_copies -= 1
        book.borrowers.append(member_id)
        member.borrowed_books[isbn] = datetime.now()
        
        self.save_data()
        return {"status": "success", "message": "Book borrowed successfully"}
    
    def return_book(self, member_id, isbn):
        """Process book return"""
        if isbn not in self.books or member_id not in self.members:
            return {"status": "error", "message": "Invalid book or member ID"}
        
        book = self.books[isbn]
        member = self.members[member_id]
        
        if isbn not in member.borrowed_books:
            return {"status": "error", "message": "Book not borrowed by this member"}
        
        # Calculate fine
        borrow_date = member.borrowed_books[isbn]
        days_borrowed = (datetime.now() - borrow_date).days
        fine = max(0, days_borrowed - self.loan_period) * self.fine_per_day
        
        book.available_copies += 1
        book.borrowers.remove(member_id)
        borrow_record = {
            "isbn": isbn,
            "title": book.title,
            "borrow_date": borrow_date.strftime("%Y-%m-%d"),
            "return_date": datetime.now().strftime("%Y-%m-%d"),
            "fine": fine
        }
        member.history.append(borrow_record)
        del member.borrowed_books[isbn]
        member.fines += fine
        
        self.save_data()
        return {
            "status": "success",
            "message": "Book returned successfully",
            "fine": fine
        }
    
    def pay_fine(self, member_id, amount):
        """Process fine payment"""
        if member_id not in self.members:
            return {"status": "error", "message": "Invalid member ID"}
        
        member = self.members[member_id]
        if amount > member.fines:
            return {"status": "error", "message": "Payment amount exceeds fine"}
        
        member.fines -= amount
        self.save_data()
        return {"status": "success", "message": f"Paid ${amount:.2f}"}
    
    def search_books(self, query, search_by="title"):
        """Search books by title, author, or category"""
        results = []
        query = query.lower()
        
        for book in self.books.values():
            if search_by == "title" and query in book.title.lower():
                results.append(book)
            elif search_by == "author" and query in book.author.lower():
                results.append(book)
            elif search_by == "category" and query in book.category.lower():
                results.append(book)
        
        return results
    
    def get_member_details(self, member_id):
        """Get detailed information about a member"""
        if member_id not in self.members:
            return {"status": "error", "message": "Invalid member ID"}
        
        member = self.members[member_id]
        current_borrows = []
        
        for isbn, borrow_date in member.borrowed_books.items():
            book = self.books[isbn]
            days_remaining = self.loan_period - (datetime.now() - borrow_date).days
            current_borrows.append({
                "title": book.title,
                "isbn": isbn,
                "borrow_date": borrow_date.strftime("%Y-%m-%d"),
                "days_remaining": days_remaining
            })
        
        return {
            "status": "success",
            "name": member.name,
            "member_id": member.member_id,
            "current_borrows": current_borrows,
            "borrow_history": member.history,
            "fines": member.fines
        }

def main():
    library = Library("Community Library")
    
    while True:
        print("\n=== Library Management System ===")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Search Books")
        print("6. Member Details")
        print("7. Pay Fine")
        print("8. Exit")
        
        choice = input("\nEnter your choice (1-8): ")
        
        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            category = input("Enter category: ")
            copies = int(input("Enter number of copies: "))
            result = library.add_book(title, author, isbn, category, copies)
            print(f"\n{result['message']}")
        
        elif choice == "2":
            name = input("Enter member name: ")
            result = library.add_member(name)
            print(f"\n{result['message']}")
            if result['status'] == 'success':
                print(f"Member ID: {result['member_id']}")
        
        elif choice == "3":
            member_id = input("Enter member ID: ")
            isbn = input("Enter book ISBN: ")
            result = library.borrow_book(member_id, isbn)
            print(f"\n{result['message']}")
        
        elif choice == "4":
            member_id = input("Enter member ID: ")
            isbn = input("Enter book ISBN: ")
            result = library.return_book(member_id, isbn)
            print(f"\n{result['message']}")
            if result['status'] == 'success' and result['fine'] > 0:
                print(f"Fine charged: ${result['fine']:.2f}")
        
        elif choice == "5":
            query = input("Enter search term: ")
            search_by = input("Search by (title/author/category): ")
            results = library.search_books(query, search_by)
            
            if results:
                print("\nSearch Results:")
                for book in results:
                    print(f"\nTitle: {book.title}")
                    print(f"Author: {book.author}")
                    print(f"ISBN: {book.isbn}")
                    print(f"Available Copies: {book.available_copies}")
            else:
                print("\nNo books found matching your search.")
        
        elif choice == "6":
            member_id = input("Enter member ID: ")
            result = library.get_member_details(member_id)
            
            if result['status'] == 'success':
                print(f"\nMember Name: {result['name']}")
                print(f"Member ID: {result['member_id']}")
                print(f"Outstanding Fine: ${result['fines']:.2f}")
                
                if result['current_borrows']:
                    print("\nCurrently Borrowed Books:")
                    for book in result['current_borrows']:
                        print(f"\nTitle: {book['title']}")
                        print(f"Borrowed on: {book['borrow_date']}")
                        print(f"Days remaining: {book['days_remaining']}")
                
                if result['borrow_history']:
                    print("\nBorrow History:")
                    for record in result['borrow_history']:
                        print(f"\nTitle: {record['title']}")
                        print(f"Borrowed: {record['borrow_date']}")
                        print(f"Returned: {record['return_date']}")
                        if record['fine'] > 0:
                            print(f"Fine charged: ${record['fine']:.2f}")
        
        elif choice == "7":
            member_id = input("Enter member ID: ")
            member = library.get_member_details(member_id)
            if member['status'] == 'success':
                print(f"Outstanding fine: ${member['fines']:.2f}")
                if member['fines'] > 0:
                    try:
                        amount = float(input("Enter payment amount: $"))
                        result = library.pay_fine(member_id, amount)
                        print(f"\n{result['message']}")
                    except ValueError:
                        print("Please enter a valid amount!")
                else:
                    print("No fine to pay!")
        
        elif choice == "8":
            print("Thank you for using the Library Management System!")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

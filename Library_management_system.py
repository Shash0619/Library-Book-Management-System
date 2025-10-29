# -------------------------------
# Library Book Management System
# -------------------------------

# Node for Linked List
class BookNode:
    def __init__(self, book_id, title, author, status="Available"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = status
        self.next = None

# Singly Linked List for Book Records
class BookList:
    def __init__(self):
        self.head = None

    def insertBook(self, book_id, title, author):
        new_book = BookNode(book_id, title, author)
        if not self.head:
            self.head = new_book
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_book
        print(f"Book '{title}' added successfully.")

    def deleteBook(self, book_id):
        temp = self.head
        prev = None
        while temp:
            if temp.book_id == book_id:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                print(f"Book ID {book_id} deleted successfully.")
                return
            prev = temp
            temp = temp.next
        print("Book not found.")

    def searchBook(self, book_id):
        temp = self.head
        while temp:
            if temp.book_id == book_id:
                print(f"\nBook Found:\nID: {temp.book_id}\nTitle: {temp.title}\nAuthor: {temp.author}\nStatus: {temp.status}")
                return temp
            temp = temp.next
        print("Book not found.")
        return None

    def displayBooks(self):
        if not self.head:
            print("No books available in the library.")
            return
        print("\nCurrent Books in Library:")
        temp = self.head
        while temp:
            print(f"ID: {temp.book_id} | Title: {temp.title} | Author: {temp.author} | Status: {temp.status}")
            temp = temp.next

# Stack for Undo Operations
class TransactionStack:
    def __init__(self):
        self.stack = []

    def push(self, transaction):
        self.stack.append(transaction)

    def pop(self):
        if not self.stack:
            return None
        return self.stack.pop()

    def display(self):
        if not self.stack:
            print("No transactions yet.")
            return
        print("\nRecent Transactions:")
        for t in reversed(self.stack):
            print(t)

# Transaction Management System
class LibrarySystem:
    def __init__(self):
        self.books = BookList()
        self.transactions = TransactionStack()

    def issueBook(self, book_id):
        book = self.books.searchBook(book_id)
        if book and book.status == "Available":
            book.status = "Issued"
            self.transactions.push(("Issue", book_id))
            print(f"Book ID {book_id} has been issued.")
        elif book:
            print("Book is already issued.")

    def returnBook(self, book_id):
        book = self.books.searchBook(book_id)
        if book and book.status == "Issued":
            book.status = "Available"
            self.transactions.push(("Return", book_id))
            print(f"Book ID {book_id} has been returned.")
        elif book:
            print("Book was not issued.")

    def undoTransaction(self):
        last = self.transactions.pop()
        if not last:
            print("No transactions to undo.")
            return

        action, book_id = last
        book = self.books.searchBook(book_id)
        if not book:
            print("Book not found for undo operation.")
            return

        if action == "Issue":
            book.status = "Available"
            print(f"Undo Successful: Book ID {book_id} issue reverted.")
        elif action == "Return":
            book.status = "Issued"
            print(f"Undo Successful: Book ID {book_id} return reverted.")

    def viewTransactions(self):
        self.transactions.display()

# -------------------------------
# Sample Run
# -------------------------------
if __name__ == "__main__":
    lib = LibrarySystem()

    lib.books.insertBook(1, "Python Basics", "John Doe")
    lib.books.insertBook(2, "Data Structures", "Jane Smith")
    lib.books.displayBooks()

    lib.issueBook(1)
    lib.returnBook(1)
    lib.viewTransactions()

    lib.undoTransaction()
    lib.books.displayBooks()

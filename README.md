# 📘 Library Book Management System (Linked List + Stack)

## 📖 Overview
This project implements a **Library Book Management System** using **Single Linked List (SLL)** and **Stack** data structures in Python.  
It helps manage a collection of books, including operations like adding, deleting, searching, issuing, returning, and undoing transactions.

It demonstrates the integration of two linear data structures — **Linked List** (for dynamic book storage) and **Stack** (for transaction history & undo operations).

---

## 🧠 Features
- Add new books to the library  
- Delete books using Book ID  
- Search for a book by its ID  
- Display all books dynamically  
- Issue or return a book  
- Undo the last issue or return transaction  
- View transaction history  

---

## 🧩 Data Structures Used
1. **Single Linked List (SLL)** – Manages the dynamic list of book records.  
2. **Stack** – Records issue and return transactions for undo functionality.  

---

## 🏗️ Class Design

### 1. BookNode (Node Structure)
Stores book details:  
- Book ID  
- Title  
- Author  
- Status (Available / Issued)

### 2. BookList (Linked List Implementation)
Implements core operations:  
- `insertBook(book_id, title, author)`  
- `deleteBook(book_id)`  
- `searchBook(book_id)`  
- `displayBooks()`

### 3. TransactionStack (Stack Implementation)
Handles transaction management:  
- `push(transaction)`  
- `pop()`  
- `viewTransactions()`

### 4. LibrarySystem (Main System Class)
Combines both structures:  
- `issueBook(book_id)`  
- `returnBook(book_id)`  
- `undoTransaction()`  
- `viewTransactions()`

---

## ⚙️ How It Works
1. The program maintains a **linked list** of books.  
2. Each issue/return action is stored in the **stack** as a transaction.  
3. The **undo operation** pops the most recent transaction from the stack and reverts it.  

---

## 🧾 Example Output
Book 'C Programming' added successfully.
Book 'Data Structures' added successfully.
Book 'Algorithms' added successfully.

Current Book List:
--------------------------------------------------
ID: 101 | Title: C Programming | Author: Dennis Ritchie | Status: Available
ID: 102 | Title: Data Structures | Author: Narasimha Karumanchi | Status: Available
ID: 103 | Title: Algorithms | Author: CLRS | Status: Available
--------------------------------------------------

Book 'C Programming' has been issued.
Book 'C Programming' has been returned.
Undo: Book 'C Programming' is now available again.

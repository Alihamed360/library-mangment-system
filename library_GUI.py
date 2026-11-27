import tkinter as tk
from tkinter import messagebox, simpledialog
books = []
root = tk.Tk()
root.title("Library Management System")
root.geometry("400x400")
def add_book():
    book = simpledialog.askstring("Add Book", "Enter book name:")
    if book:
        books.append(book)
        messagebox.showinfo("Success", "Book added!")
def view_books():
    if books:
        messagebox.showinfo("Books", "\n".join(books))
    else:
        messagebox.showinfo("Books", "No books yet")
def search_book():
    book = simpledialog.askstring("Search Book", "Enter book name:")
    if book:
        for b in books:
            if book.lower() in b.lower():
                messagebox.showinfo("Found", b)
                return
        messagebox.showinfo("Search", "Book not found")
title = tk.Label(
    root,
    text="Library Management System",
    font=("Arial", 16, "bold")
)
title.pack(pady=20)
tk.Button(
    root,
    text="Add Book",
    command=add_book
).pack(pady=10)
tk.Button(
    root,
    text="View Books",
    command=view_books
).pack(pady=10)
tk.Button(
    root,
    text="Search Book",
    command=search_book
).pack(pady=10)
tk.Button(
    root,
    text="Exit",
    command=root.destroy
).pack(pady=10)
root.mainloop()
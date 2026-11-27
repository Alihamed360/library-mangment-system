import tkinter as tk
from tkinter import messagebox, simpledialog

books = []

root = tk.Tk()
root.title("Library Management System")
root.geometry("500x400")


def add_book():
    book = simpledialog.askstring("Add Book", "Enter book name:")

    if book:
        books.append(book)
        messagebox.showinfo("Success", "Book added successfully!")


def view_books():
    if books:
        messagebox.showinfo("Books", "\n".join(books))
    else:
        messagebox.showinfo("Books", "No books yet")


def search_book():
    book = simpledialog.askstring("Search Book", "Enter book name:")

    if book:
        if book in books:
            messagebox.showinfo("Search", "Book found!")
        else:
            messagebox.showinfo("Search", "Book not found")


def delete_book():
    book = simpledialog.askstring("Delete Book", "Enter book name:")

    if book:
        if book in books:
            books.remove(book)
            messagebox.showinfo("Success", "Book deleted!")
        else:
            messagebox.showinfo("Error", "Book not found")


title = tk.Label(
    root,
    text="Library Management System",
    font=("Arial", 18, "bold")
)
title.pack(pady=20)

tk.Button(root, text="Add Book", width=20, command=add_book).pack(pady=5)

tk.Button(root, text="View Books", width=20, command=view_books).pack(pady=5)

tk.Button(root, text="Search Book", width=20, command=search_book).pack(pady=5)

tk.Button(root, text="Delete Book", width=20, command=delete_book).pack(pady=5)

tk.Button(root, text="Exit", width=20, command=root.destroy).pack(pady=5)

root.mainloop()
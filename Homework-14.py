#Homework-14


import json, requests

#1.write a Python script that reads the students.jon JSON file and prints details of each student.
filename = 'students.json'

with open(filename) as f:
    data = json.load(f)
    print(data)

#2.Task: Weather API


#3.Write a program that allows users to add new books,
# update existing book information, and delete books from the books.json JSON file.

BOOKS_FILE = "books.json"

def load_books():
    with open(BOOKS_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            print(f"{BOOKS_FILE} file is not found.")

def save_books(books):
    with open(BOOKS_FILE, "w") as file:
        json.dump(books, file, indent=4)

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = input("Enter publication year: ")
    books = load_books()
    books.append({"title": title, "author": author, "year": year})
    save_books(books)
    print(f"Book '{title}' added successfully!")

def update_book():
    books = load_books()
    title = input("Enter the title of the book to update: ")

    for book in books:
        if book["title"].lower() == title.lower():
            print("Enter new details (leave blank to keep existing values):")
            new_author = input(f"New author [{book['author']}]: ") or book["author"]
            new_year = input(f"New year [{book['year']}]: ") or book["year"]


            book["author"], book["year"], book["isbn"] = new_author, new_year
            save_books(books)
            print(f"Book '{title}' updated successfully!")
            return

    print("Book not found.")

def delete_book():
    books = load_books()
    title = input("Enter the title of the book to delete: ")

    for book in books:
        if book["title"].lower() == title.lower():
            books.remove(book)
            save_books(books)
            print(f"Book '{title}' deleted successfully!")
            return

    print("Book not found.")


def main():
    while True:
        print("\nBook Manager")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            update_book()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

#4. Task: Movie Recommendation System

# Library Management System

library = {}

def add_book(title, author):
    library[title] = {
        "author": author,
        "available": True
    }
    print(f'"{title}" added successfully.')

def view_books():
    if not library:
        print("Library is empty.")
        return
    for title, info in library.items():
        status = "Available" if info["available"] else "Issued"
        print(f'Title: {title}, Author: {info["author"]}, Status: {status}')


def issue_book(title):
    if title in library and library[title]["available"]:
        library[title]["available"] = False
        print(f'"{title}" issued successfully.')
    else:
        print("Book not available.")


def return_book(title):
    if title in library and not library[title]["available"]:
        library[title]["available"] = True
        print(f'"{title}" returned successfully.')
    else:
        print("Invalid return.")


def menu():
    while True:
        print("\n1. Add Book")
        print("2. View Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            add_book(title, author)

        elif choice == "2":
            view_books()

        elif choice == "3":
            title = input("Enter title to issue: ")
            issue_book(title)

        elif choice == "4":
            title = input("Enter title to return: ")
            return_book(title)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")
menu()

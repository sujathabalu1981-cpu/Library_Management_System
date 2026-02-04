print("welcome to the library Management system")
print("1. Add a book")
print("2. Remove a book")
print("3. View all books")
books = []  
while True:
    choice = input("Enter your choice (1-3) or 'q' to quit: ")
    if choice == '1':
        book_name = input("Enter the name of the book: ")
        books.append(book_name)
        print(f"'{book_name}' has been added to the library.")
    elif choice == '2':
        book_name = input("Enter the name of the book to remove: ")
        if book_name in books:
            books.remove(book_name)
            print(f"'{book_name}' has been removed from the library.")
        else:
            print(f"'{book_name}' not found in the library.")
    elif choice == '3':
        if books:
            print("Books in the library:")
            for book in books:
                print(f"- {book}")
        else:
            print("No books in the library.")
    elif choice.lower() == 'q':
        print("Exiting the library management system. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 3, or 'q' to quit.") 
        
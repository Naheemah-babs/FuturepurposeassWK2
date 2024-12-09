# books in the library

library_books = ["python basics", "data science 101", "ai for beginners"]
borrowed_books = []

def view_books():
    if library_books:
        print(f"Available books are {library_books} \n")
    else:
         print("No books are currently available. \n")

# function to borrow books
def borrow_book():
    user_borrowed_book = input("which book will you like to borrow? \n").lower()
    if user_borrowed_book in library_books:
        print(f"you have successfully borrowed {user_borrowed_book}")
        library_books.remove(user_borrowed_book)
        borrowed_books.append(user_borrowed_book)
    else:
        print("that book is not available")

# function to return books
def return_book():
    user_returned_book = input('which book are you returning?\n').lower()
    if user_returned_book in borrowed_books:
        library_books.append(user_returned_book)
        print(f"you have successfully returned {user_returned_book}")
        borrowed_books.remove(user_returned_book)
    else:
        print("the book you are trying to return is not from this library")

def library():
    print("Welcome to the Library! \n\n")
    user_choice = input("what will you like to do today?\n\n" 
                "Press 1 to View available books\n"
                "Press 2 to Borrow a book \n"
                "Press 3 to Return a book \n"
                "Press 4 to Exit \n\n")
    if user_choice == "1":
            view_books()
    while True:
        user_choice = input( 
                "Press 1 to View available books\n"
                "Press 2 to Borrow a book \n"
                "Press 3 to Return a book \n"
                "Press 4 to Exit \n\n")   
        if user_choice == "1":
            view_books()
        elif user_choice == "2":
            borrow_book()
        elif user_choice == "3":
            return_book()
        elif user_choice == "4":
            print("Thank you for visiting the library")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
            

library()